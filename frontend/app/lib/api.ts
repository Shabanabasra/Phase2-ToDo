// API utility functions for interacting with the backend

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface Todo {
  id: string;
  title: string;
  description?: string;
  is_completed: boolean;
  user_id: string;
  created_at: string;
  updated_at: string;
}

interface TodoCreate {
  title: string;
  description?: string;
}

interface TodoUpdate {
  title?: string;
  description?: string;
  is_completed?: boolean;
}

// Get authorization header
const getAuthHeader = (): Record<string, string> => {
  const token = localStorage.getItem('access_token');
  if (token) {
    return { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' };
  }
  return { 'Content-Type': 'application/json' };
};

// Get current user ID from token
const getCurrentUserId = (): string | null => {
  const token = localStorage.getItem('access_token');
  if (!token) return null;

  try {
    // Decode JWT token to get user ID
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(
      atob(base64)
        .split('')
        .map(c => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2))
        .join('')
    );

    const payload = JSON.parse(jsonPayload);
    return payload.sub;
  } catch (error) {
    console.error('Error decoding token:', error);
    return null;
  }
};

// Auth API functions
export const authAPI = {
  login: async (email: string, password: string) => {
    const response = await fetch(`${API_BASE_URL}/api/auth/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username: email, password }),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Login failed');
    }

    return response.json();
  },

  register: async (email: string, password: string) => {
    const response = await fetch(`${API_BASE_URL}/api/auth/register`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email, password }),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Registration failed');
    }

    return response.json();
  },
};

// Todo API functions
export const todoAPI = {
  getTodos: async () => {
    const userId = getCurrentUserId();
    if (!userId) {
      throw new Error('User not authenticated');
    }

    const response = await fetch(`${API_BASE_URL}/api/${userId}/tasks`, {
      headers: getAuthHeader(),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Failed to fetch todos');
    }

    return response.json();
  },

  createTodo: async (todo: TodoCreate) => {
    const userId = getCurrentUserId();
    if (!userId) {
      throw new Error('User not authenticated');
    }

    const response = await fetch(`${API_BASE_URL}/api/${userId}/tasks`, {
      method: 'POST',
      headers: getAuthHeader(),
      body: JSON.stringify(todo),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Failed to create todo');
    }

    return response.json();
  },

  updateTodo: async (id: string, todo: TodoUpdate) => {
    const userId = getCurrentUserId();
    if (!userId) {
      throw new Error('User not authenticated');
    }

    const response = await fetch(`${API_BASE_URL}/api/${userId}/tasks/${id}`, {
      method: 'PUT',
      headers: getAuthHeader(),
      body: JSON.stringify(todo),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Failed to update todo');
    }

    return response.json();
  },

  deleteTodo: async (id: string) => {
    const userId = getCurrentUserId();
    if (!userId) {
      throw new Error('User not authenticated');
    }

    const response = await fetch(`${API_BASE_URL}/api/${userId}/tasks/${id}`, {
      method: 'DELETE',
      headers: getAuthHeader(),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Failed to delete todo');
    }

    return response.json();
  },

  toggleTodoCompletion: async (id: string, isCompleted: boolean) => {
    const userId = getCurrentUserId();
    if (!userId) {
      throw new Error('User not authenticated');
    }

    const response = await fetch(`${API_BASE_URL}/api/${userId}/tasks/${id}/complete`, {
      method: 'PATCH',
      headers: getAuthHeader(),
      body: JSON.stringify({ is_completed: isCompleted }),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Failed to update todo completion status');
    }

    return response.json();
  },
};