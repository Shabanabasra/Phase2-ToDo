'use client';

import { useState, useEffect } from 'react';
import { useAuth } from '@/app/context/auth-context';
import TodoList from '@/app/components/TodoList';
import TodoForm from '@/app/components/TodoForm';
import AuthForm from '@/app/components/AuthForm';

export default function Home() {
  const { user, loading } = useAuth();
  const [showAuth, setShowAuth] = useState(false);

  if (loading) {
    return <div className="flex justify-center items-center h-screen">Loading...</div>;
  }

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-4xl mx-auto px-4">
        <header className="flex justify-between items-center mb-8">
          <h1 className="text-3xl font-bold text-gray-800">Todo App</h1>
          {user ? (
            <div className="flex items-center space-x-4">
              <span className="text-gray-600">Welcome, {user.email}</span>
              <button
                onClick={() => setShowAuth(true)}
                className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded"
              >
                {showAuth ? 'Hide' : 'Show'} Auth
              </button>
            </div>
          ) : (
            <button
              onClick={() => setShowAuth(true)}
              className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded"
            >
              Login / Register
            </button>
          )}
        </header>

        {showAuth && !user && (
          <div className="mb-8 p-6 bg-white rounded-lg shadow">
            <AuthForm />
          </div>
        )}

        {user ? (
          <div className="bg-white rounded-lg shadow p-6">
            <TodoForm />
            <TodoList />
          </div>
        ) : (
          <div className="text-center py-12">
            <h2 className="text-xl text-gray-600 mb-4">Please log in to manage your todos</h2>
            <p className="text-gray-500">Sign in or create an account to get started</p>
          </div>
        )}
      </div>
    </div>
  );
}