# Quickstart Guide: Todo Full-Stack Web Application

## Prerequisites

- Node.js 18+ installed
- Python 3.11+ installed
- PostgreSQL database (Neon Serverless recommended)
- `uv` package manager for Python
- Git

## Environment Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create the root `.env` file with the following variables:
```env
DATABASE_URL="postgresql://username:password@host:port/database_name"
BETTER_AUTH_SECRET="your-super-secret-jwt-key-here-with-at-least-32-characters"
NEXT_PUBLIC_API_URL="http://localhost:8000"
JWT_ALGORITHM="HS256"
```

## Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create and activate a Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies using uv:
```bash
uv pip install -r requirements.txt
# Or if uv is not available:
pip install -r requirements.txt
```

4. Run database migrations:
```bash
alembic upgrade head
```

5. Start the backend server:
```bash
uvicorn src.main:app --reload --port 8000
```

The backend will be available at `http://localhost:8000`.

## Frontend Setup

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

The frontend will be available at `http://localhost:3000`.

## API Endpoints

Once both servers are running, the following endpoints will be available:

### Authentication
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout

### Todo Management (requires authentication)
- `GET /api/{user_id}/tasks` - Get all user's tasks
- `POST /api/{user_id}/tasks` - Create new task
- `GET /api/{user_id}/tasks/{id}` - Get specific task
- `PUT /api/{user_id}/tasks/{id}` - Update task
- `DELETE /api/{user_id}/tasks/{id}` - Delete task
- `PATCH /api/{user_id}/tasks/{id}/complete` - Toggle completion status

## Development

### Running Tests
Backend tests:
```bash
cd backend
pytest
```

Frontend tests:
```bash
cd frontend
npm test
```

### Environment Variables
- `DATABASE_URL`: PostgreSQL connection string
- `BETTER_AUTH_SECRET`: Secret key for JWT signing
- `NEXT_PUBLIC_API_URL`: Base URL for API calls from frontend
- `JWT_ALGORITHM`: Algorithm for JWT signing (default: HS256)

## Database Migrations

To create a new migration:
```bash
cd backend
alembic revision --autogenerate -m "Description of changes"
```

To apply migrations:
```bash
alembic upgrade head
```

## Production Deployment

1. Set environment variables for production
2. Build the frontend: `npm run build`
3. Deploy backend with production server (e.g., gunicorn)
4. Serve frontend build through a web server (e.g., nginx)