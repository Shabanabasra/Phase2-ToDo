from sqlmodel import Session, select
from typing import List, Optional
from ..models.todo import Todo, TodoCreate, TodoUpdate
from ..models.user import User

def create_todo(session: Session, todo: TodoCreate, user_id: str) -> Todo:
    """Create a new todo for a user."""
    db_todo = Todo(**todo.dict(), user_id=user_id)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

def get_todos(session: Session, user_id: str, limit: int = 50, offset: int = 0) -> List[Todo]:
    """Get all todos for a specific user."""
    statement = select(Todo).where(Todo.user_id == user_id).offset(offset).limit(limit)
    todos = session.exec(statement).all()
    return todos

def get_todo(session: Session, todo_id: str, user_id: str) -> Optional[Todo]:
    """Get a specific todo for a user."""
    statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == user_id)
    todo = session.exec(statement).first()
    return todo

def update_todo(session: Session, todo_id: str, todo_update: TodoUpdate, user_id: str) -> Optional[Todo]:
    """Update a specific todo for a user."""
    statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == user_id)
    db_todo = session.exec(statement).first()

    if not db_todo:
        return None

    # Update the fields that are provided
    for field, value in todo_update.dict(exclude_unset=True).items():
        setattr(db_todo, field, value)

    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

def delete_todo(session: Session, todo_id: str, user_id: str) -> bool:
    """Delete a specific todo for a user."""
    statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == user_id)
    db_todo = session.exec(statement).first()

    if not db_todo:
        return False

    session.delete(db_todo)
    session.commit()
    return True

def toggle_todo_completion(session: Session, todo_id: str, is_completed: bool, user_id: str) -> Optional[Todo]:
    """Toggle the completion status of a specific todo for a user."""
    statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == user_id)
    db_todo = session.exec(statement).first()

    if not db_todo:
        return None

    db_todo.is_completed = is_completed
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo