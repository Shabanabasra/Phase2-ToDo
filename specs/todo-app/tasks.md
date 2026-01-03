# Engineering Tasks: Todo Full-Stack Web Application

## Task Breakdown

### PHASE 1 — Project Setup

**Task 1.1: Create project structure**
- [X] Create backend/ directory
- [X] Create frontend/ directory
- [X] Create root .env file with template variables
- [X] Verify monorepo structure

**Task 1.2: Initialize backend environment**
- [ ] Create Python virtual environment in backend/
- [ ] Create requirements.txt file
- [ ] Install dependencies using uv
- [ ] Set up gitignore for Python files

**Task 1.3: Initialize frontend environment**
- [ ] Create Next.js 16 app in frontend/ directory
- [ ] Install required frontend dependencies
- [ ] Set up gitignore for Node.js files
- [ ] Configure basic project structure

### PHASE 2 — Backend Setup

**Task 2.1: Install backend dependencies**
- [X] `uv add fastapi`
- [X] `uv add sqlmodel`
- [X] `uv add psycopg2-binary`
- [X] `uv add python-dotenv`
- [X] `uv add pydantic`
- [X] `uv add python-jose[cryptography]`
- [X] `uv add bcrypt`
- [X] `uv add alembic`
- [X] Verify all dependencies are installed correctly

**Task 2.2: Configure environment variables**
- [X] Create .env file at project root
- [X] Add DATABASE_URL variable
- [X] Add BETTER_AUTH_SECRET variable
- [X] Add JWT_ALGORITHM variable
- [X] Implement python-dotenv loading in backend

**Task 2.3: Create database engine and session**
- [X] Create database engine with PostgreSQL connection
- [X] Implement session management
- [X] Create database connection utilities
- [X] Test database connection

**Task 2.4: Define User and Todo models**
- [X] Create User model with email, hashed password, timestamps
- [X] Create Todo model with title, description, completion status, user relationship
- [X] Implement proper relationships between User and Todo
- [X] Add validation rules to models
- [X] Create Pydantic schemas for request/response

**Task 2.5: Implement JWT verification middleware**
- [X] Create JWT token creation function
- [X] Create JWT token verification dependency
- [X] Implement token expiration handling
- [X] Add proper error handling for invalid tokens

**Task 2.6: Build authentication endpoints**
- [X] Create registration endpoint with password hashing
- [X] Create login endpoint with JWT token generation
- [X] Create logout endpoint
- [X] Implement proper error responses

**Task 2.7: Build CRUD endpoints for todos**
- [X] Create GET /api/{user_id}/tasks endpoint
- [X] Create POST /api/{user_id}/tasks endpoint
- [X] Create GET /api/{user_id}/tasks/{id} endpoint
- [X] Create PUT /api/{user_id}/tasks/{id} endpoint
- [X] Create DELETE /api/{user_id}/tasks/{id} endpoint
- [X] Create PATCH /api/{user_id}/tasks/{id}/complete endpoint

**Task 2.8: Enforce user ownership and isolation**
- [X] Add user_id validation in all endpoints
- [X] Verify JWT token user matches URL user_id
- [X] Check that todos belong to the authenticated user
- [X] Return 403 for unauthorized access attempts
- [X] Implement proper authorization checks

### PHASE 3 — Frontend Setup

**Task 3.1: Create Next.js application**
- [X] Run `npx create-next-app@16 frontend`
- [X] Configure TypeScript if needed
- [X] Set up basic project structure
- [X] Install Tailwind CSS

**Task 3.2: Install Better Auth**
- [X] Install Better Auth package
- [X] Configure JWT plugin
- [X] Set up authentication provider
- [X] Configure with BETTER_AUTH_SECRET

**Task 3.3: Create authentication pages**
- [X] Create login page component
- [X] Create signup page component
- [X] Implement form validation
- [X] Add error handling and user feedback

**Task 3.4: Create Todo dashboard**
- [X] Create dashboard page component
- [X] Implement todo list display
- [X] Create todo creation form
- [X] Add todo editing functionality
- [X] Implement todo deletion
- [X] Add completion toggle functionality

**Task 3.5: Create API client**
- [X] Create API service with base URL
- [X] Implement function to attach JWT to API calls
- [X] Create functions for all required API endpoints
- [X] Add error handling for API calls

**Task 3.6: Implement responsive styling**
- [X] Apply Tailwind CSS classes for responsive design
- [X] Create mobile-friendly layouts
- [X] Ensure proper styling across different screen sizes
- [X] Add accessibility features

### PHASE 4 — Auth Integration

**Task 4.1: Configure shared BETTER_AUTH_SECRET**
- [X] Ensure same secret is used in frontend and backend
- [X] Verify JWT configuration consistency
- [X] Test token generation and validation

**Task 4.2: Implement JWT validation in FastAPI**
- [X] Create dependency for JWT token validation
- [X] Add middleware to validate tokens on protected routes
- [X] Handle expired tokens appropriately
- [X] Return proper error responses for invalid tokens

**Task 4.3: Enforce user isolation**
- [X] Verify user_id from JWT matches the requested user_id
- [X] Implement checks in all todo endpoints
- [X] Test that users cannot access other users' data
- [X] Add proper authorization guards

### PHASE 5 — Testing & Validation

**Task 5.1: Unit tests for backend**
- [ ] Write unit tests for User model
- [ ] Write unit tests for Todo model
- [ ] Write unit tests for authentication functions
- [ ] Write unit tests for JWT verification
- [ ] Write unit tests for authorization logic

**Task 5.2: Integration tests**
- [ ] Write integration tests for authentication flow
- [ ] Write integration tests for CRUD operations
- [ ] Test user isolation functionality
- [ ] Test error handling scenarios

**Task 5.3: Frontend tests**
- [ ] Write tests for authentication components
- [ ] Write tests for todo dashboard components
- [ ] Test API client functionality
- [ ] Test user interaction flows

**Task 5.4: Security testing**
- [ ] Test that users cannot access other users' todos
- [ ] Test authentication bypass attempts
- [ ] Verify proper error responses
- [ ] Test JWT token validation

**Task 5.5: Responsive design validation**
- [ ] Test UI on different screen sizes
- [ ] Verify mobile responsiveness
- [ ] Test touch interactions on mobile
- [ ] Validate accessibility features

### PHASE 6 — Deployment Preparation

**Task 6.1: Environment configuration**
- [ ] Create production environment variables
- [ ] Set up database connection for production
- [ ] Configure authentication for production

**Task 6.2: Build and optimization**
- [ ] Create production build for frontend
- [ ] Optimize assets and dependencies
- [ ] Set up deployment configuration