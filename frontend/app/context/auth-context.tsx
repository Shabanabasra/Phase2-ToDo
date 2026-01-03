'use client';

import { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { jwtDecode } from 'jwt-decode';

interface User {
  id: string;
  email: string;
  created_at: string;
}

interface AuthContextType {
  user: User | null;
  loading: boolean;
  login: (email: string, password: string) => Promise<void>;
  register: (email: string, password: string) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem('access_token');
    if (token) {
      try {
        const decoded: any = jwtDecode(token);
        if (decoded.exp * 1000 > Date.now()) {
          fetchUserDetails(token);
        } else {
          localStorage.removeItem('access_token');
        }
      } catch (error) {
        console.error('Error decoding token:', error);
        localStorage.removeItem('access_token');
      }
    }
    setLoading(false);
  }, []);

  const fetchUserDetails = async (token: string) => {
    try {
      const decoded: any = jwtDecode(token);
      const userId = decoded.sub;

      setUser({
        id: userId,
        email: decoded.email || 'user@example.com',
        created_at: decoded.created_at || new Date().toISOString()
      });
    } catch (error) {
      console.error('Error decoding token:', error);
      localStorage.removeItem('access_token');
    }
  };

  // ---------- LOGIN UPDATE ----------
  const login = async (email: string, password: string) => {
    const formData = new URLSearchParams();
    formData.append('grant_type', 'password');
    formData.append('username', email);
    formData.append('password', password);
    formData.append('scope', '');
    formData.append('client_id', '');
    formData.append('client_secret', '');

    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/auth/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: formData.toString(),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || 'Login failed');
    }

    const data = await response.json();
    const { access_token } = data;

    localStorage.setItem('access_token', access_token);
    fetchUserDetails(access_token);
  };

  // ---------- REGISTER UPDATE ----------
  const register = async (email: string, password: string) => {
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/auth/register`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email, password }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || 'Registration failed');
    }

    const userData = await response.json();
    return userData;
  };

  const logout = () => {
    localStorage.removeItem('access_token');
    setUser(null);
  };

  const value = { user, loading, login, register, logout };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}