from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List
import uuid

from app.database import get_session
from app.models.todo_models import Todo, TodoCreate, TodoRead, TodoUpdate, User
from app.auth.auth_handler import get_current_user

router = APIRouter()

@router.get("/", response_model=List[TodoRead])
def read_todos(
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
    skip: int = 0,
    limit: int = 100
):
    """
    Retrieve todos for the current user.
    """
    statement = select(Todo).where(Todo.owner_id == current_user.id).offset(skip).limit(limit)
    todos = session.exec(statement).all()
    return todos

@router.post("/", response_model=TodoRead)
def create_todo(
    todo: TodoCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Create a new todo for the current user.
    """
    db_todo = Todo.model_validate({**todo.model_dump(), "owner_id": current_user.id})
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

@router.get("/{todo_id}", response_model=TodoRead)
def read_todo(
    todo_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Get a specific todo by ID.
    """
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    if todo.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this todo"
        )
    return todo

@router.put("/{todo_id}", response_model=TodoRead)
def update_todo(
    todo_id: uuid.UUID,
    todo_update: TodoUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Update a specific todo by ID.
    """
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    if todo.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this todo"
        )

    # Update todo fields
    for field, value in todo_update.dict(exclude_unset=True).items():
        setattr(todo, field, value)

    todo.updated_at = todo.__class__.updated_at.default_factory()
    session.add(todo)
    session.commit()
    session.refresh(todo)

    return todo

@router.delete("/{todo_id}")
def delete_todo(
    todo_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Delete a specific todo by ID.
    """
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    if todo.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this todo"
        )

    session.delete(todo)
    session.commit()
    return {"message": "Todo deleted successfully"}