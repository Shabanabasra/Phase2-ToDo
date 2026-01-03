# Todo Full-Stack Web Application

A modern, responsive, multi-user todo web application with persistent storage and authentication.

## Tech Stack

### Frontend:
- Next.js 16+ (App Router)
- TypeScript
- Tailwind CSS
- JWT-based authentication

### Backend:
- Python 3.11+
- FastAPI
- SQLModel
- PostgreSQL (Neon Serverless)
- psycopg2
- python-dotenv
- JWT verification

## Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL database (Neon Serverless used in this example)

## Setup Instructions

### 1. Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate

   pip install -r requirements.txt
   ```

3. Make sure your `.env` file is properly configured in the root directory with:
   ```env
   DATABASE_URL=postgresql+psycopg2://...
   BETTER_AUTH_SECRET=your_shared_secret
   NEXT_PUBLIC_API_URL=http://localhost:8000
   JWT_ALGORITHM=HS256
   ```

4. Start the backend server:
   ```bash
   python run.py
   ```
   The backend will be running on `http://localhost:8000`

### 2. Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```
   The frontend will be running on `http://localhost:3000`

## Features

- User registration and authentication
- Create, read, update, and delete todos
- Set priority levels (Low, Medium, High)
- Set due dates for tasks
- User-specific task management (users can only access their own tasks)
- Responsive UI that works on desktop and mobile devices

## API Endpoints

### Authentication
- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login and get JWT token

### Users
- `GET /users/me` - Get current user details
- `GET /users/{user_id}` - Get user details (current user only)
- `PATCH /users/{user_id}` - Update user details (current user only)

### Todos
- `GET /todos/` - Get all todos for the current user
- `POST /todos/` - Create a new todo for the current user
- `GET /todos/{todo_id}` - Get a specific todo (user's own todo only)
- `PUT /todos/{todo_id}` - Update a specific todo (user's own todo only)
- `DELETE /todos/{todo_id}` - Delete a specific todo (user's own todo only)

## Security Features

- JWT-based authentication for all API routes
- Users can only access their own data
- Passwords are hashed using bcrypt
- Input validation and sanitization

## Environment Variables

The application uses the following environment variables (set in the root `.env` file):

- `DATABASE_URL` - PostgreSQL database connection string
- `BETTER_AUTH_SECRET` - Secret key for JWT token signing
- `NEXT_PUBLIC_API_URL` - Backend API URL for frontend
- `JWT_ALGORITHM` - JWT algorithm (default: HS256)

## Project Structure

```
Todo/
├── frontend/              # Next.js 16 App Router frontend
│   ├── app/               # Application routes and components
│   ├── components/        # Reusable React components
│   ├── context/           # React context providers
│   ├── lib/               # Utility functions
│   ├── package.json
│   └── next.config.ts
├── backend/               # FastAPI backend
│   ├── app/
│   │   ├── models/        # SQLModel database models
│   │   ├── schemas/       # Pydantic schemas
│   │   ├── database/      # Database configuration
│   │   ├── api/           # API route handlers
│   │   └── auth/          # Authentication handlers
│   ├── main.py            # Main FastAPI application
│   ├── requirements.txt
│   └── run.py             # Run script
├── .env                   # Environment variables (shared)
└── README.md              # This file
```

## Development

To run both frontend and backend simultaneously during development:

1. Start the backend server in one terminal:
   ```bash
   cd backend
   python run.py
   ```

2. Start the frontend server in another terminal:
   ```bash
   cd frontend
   npm run dev
   ```

## Database Models

### User
- `id`: UUID (Primary Key)
- `email`: String (Unique, Indexed)
- `name`: String
- `hashed_password`: String
- `is_active`: Boolean (Default: true)
- `created_at`: DateTime

### Todo
- `id`: UUID (Primary Key)
- `title`: String
- `description`: String (Optional)
- `is_completed`: Boolean (Default: false)
- `priority`: Integer (1: low, 2: medium, 3: high)
- `due_date`: DateTime (Optional)
- `owner_id`: UUID (Foreign Key to User)
- `created_at`: DateTime
- `updated_at`: DateTime"# Phase2-ToDo" 
