# Data Model: Todo Full-Stack Web Application

## User Entity

### Fields
- **id**: UUID (Primary Key, auto-generated)
- **email**: String (Unique, Required, Validated as email format)
- **hashed_password**: String (Required, Hashed with bcrypt)
- **created_at**: DateTime (Auto-generated on creation)
- **updated_at**: DateTime (Auto-generated on update)

### Relationships
- **todos**: One-to-Many relationship with Todo entity (User has many Todos)

### Validation Rules
- Email must follow standard email format
- Email must be unique across all users
- Password must meet complexity requirements before hashing
- All required fields must be present during creation

## Todo Entity

### Fields
- **id**: UUID (Primary Key, auto-generated)
- **title**: String (Required, Max length 255)
- **description**: Text (Optional, Max length 1000)
- **is_completed**: Boolean (Default: False)
- **user_id**: UUID (Foreign Key to User.id, Required)
- **created_at**: DateTime (Auto-generated on creation)
- **updated_at**: DateTime (Auto-generated on update)

### Relationships
- **user**: Many-to-One relationship with User entity (Todo belongs to one User)

### Validation Rules
- Title is required and cannot be empty
- Title must be less than 255 characters
- Description, if provided, must be less than 1000 characters
- user_id must reference an existing User
- is_completed defaults to False when creating new todos

## State Transitions

### Todo Completion States
- **Initial State**: is_completed = False (default when created)
- **Transition**: is_completed can be toggled between True and False
- **Rules**: Only the owner of the todo can change its completion status

### User Authentication States
- **Registered**: User exists in database with hashed credentials
- **Active Session**: Valid JWT token exists and hasn't expired
- **Inactive**: Token expired or user deleted

## Database Constraints

### Referential Integrity
- Foreign key constraint on user_id in todos table referencing users.id
- Cascade delete not enabled to prevent accidental todo deletion when user is removed
- All foreign key references must point to existing records

### Indexes
- Index on users.email for fast login lookups
- Index on todos.user_id for efficient user-specific queries
- Composite index on (todos.user_id, todos.created_at) for efficient user todo retrieval with sorting

## Security Considerations

### Data Access
- Todos are accessible only by their owner (user_id matching authenticated user)
- No direct access to other users' todos through any API endpoint
- All queries must be parameterized to prevent SQL injection

### Data Validation
- Input validation at both API and database levels
- Length constraints to prevent oversized data storage
- Format validation for email fields