'use client';

import { useState, useEffect } from 'react';
import { todoAPI } from '@/app/lib/api';

interface Todo {
  id: string;
  title: string;
  description?: string;
  is_completed: boolean;
  user_id: string;
  created_at: string;
  updated_at: string;
}

export default function TodoList() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [loading, setLoading] = useState(true);
  const [editingId, setEditingId] = useState<string | null>(null);
  const [editText, setEditText] = useState('');

  useEffect(() => {
    fetchTodos();
  }, []);

  const fetchTodos = async () => {
    try {
      const data = await todoAPI.getTodos();
      setTodos(data);
    } catch (error) {
      console.error('Error fetching todos:', error);
    } finally {
      setLoading(false);
    }
  };

  const toggleTodo = async (id: string, currentStatus: boolean) => {
    try {
      const updatedTodo = await todoAPI.toggleTodoCompletion(id, !currentStatus);
      setTodos(todos.map(todo =>
        todo.id === id ? updatedTodo : todo
      ));
    } catch (error) {
      console.error('Error updating todo:', error);
    }
  };

  const deleteTodo = async (id: string) => {
    if (!confirm('Are you sure you want to delete this todo?')) return;

    try {
      await todoAPI.deleteTodo(id);
      setTodos(todos.filter(todo => todo.id !== id));
    } catch (error) {
      console.error('Error deleting todo:', error);
    }
  };

  const startEditing = (id: string, title: string) => {
    setEditingId(id);
    setEditText(title);
  };

  const saveEdit = async (id: string) => {
    if (!editText.trim()) return;

    try {
      const updatedTodo = await todoAPI.updateTodo(id, { title: editText });
      setTodos(todos.map(todo =>
        todo.id === id ? updatedTodo : todo
      ));
      setEditingId(null);
      setEditText('');
    } catch (error) {
      console.error('Error updating todo:', error);
    }
  };


  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString();
  };

  if (loading) {
    return <div className="text-center py-4">Loading todos...</div>;
  }

  return (
    <div>
      <h2 className="text-xl font-semibold mb-4">Your Todos</h2>

      {todos.length === 0 ? (
        <div className="text-center py-8 text-gray-500">
          <p>No todos yet. Add one above to get started!</p>
        </div>
      ) : (
        <ul className="space-y-3">
          {todos.map(todo => (
            <li
              key={todo.id}
              className={`p-4 border rounded-lg flex items-start justify-between ${todo.is_completed ? 'bg-gray-100' : 'bg-white'}`}
            >
              <div className="flex items-start space-x-3 flex-1">
                <input
                  type="checkbox"
                  checked={todo.is_completed}
                  onChange={() => toggleTodo(todo.id, todo.is_completed)}
                  className="mt-1 h-5 w-5 rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                />

                <div className="flex-1">
                  {editingId === todo.id ? (
                    <div className="flex space-x-2">
                      <input
                        type="text"
                        value={editText}
                        onChange={(e) => setEditText(e.target.value)}
                        className="flex-1 px-2 py-1 border border-gray-300 rounded focus:outline-none focus:ring-blue-500"
                        autoFocus
                      />
                      <button
                        onClick={() => saveEdit(todo.id)}
                        className="bg-green-500 text-white px-3 py-1 rounded"
                      >
                        Save
                      </button>
                      <button
                        onClick={() => setEditingId(null)}
                        className="bg-gray-500 text-white px-3 py-1 rounded"
                      >
                        Cancel
                      </button>
                    </div>
                  ) : (
                    <div>
                      <div>
                        <span
                          className={`text-lg ${todo.is_completed ? 'line-through text-gray-500' : 'text-gray-800'}`}
                          onClick={() => startEditing(todo.id, todo.title)}
                        >
                          {todo.title}
                        </span>
                      </div>

                      {todo.description && (
                        <p className="text-gray-600 mt-1">{todo.description}</p>
                      )}
                    </div>
                  )}
                </div>
              </div>

              <div className="flex space-x-2">
                {editingId !== todo.id && (
                  <button
                    onClick={() => startEditing(todo.id, todo.title)}
                    className="text-blue-500 hover:text-blue-700"
                  >
                    Edit
                  </button>
                )}
                <button
                  onClick={() => deleteTodo(todo.id)}
                  className="text-red-500 hover:text-red-700"
                >
                  Delete
                </button>
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}