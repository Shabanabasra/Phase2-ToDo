from typing import List
from uuid import UUID
from sqlmodel import Session
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from ..database.session import get_session
from ..models.todo import Todo, TodoCreate, TodoRead, TodoUpdate
from ..models.user import User
from ..services.todo_service import (
    create_todo, get_todos, get_todo, update_todo, delete_todo, toggle_todo_completion
)
from ..services.auth import get_current_user

class ToggleCompletionRequest(BaseModel):
    is_completed: bool

router = APIRouter(prefix="/api/{user_id}", tags=["Todos"])

def validate_user_ownership(current_user: dict, user_id: str):
    """Validate that the authenticated user matches the requested user_id."""
    if str(current_user.get("sub")) != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this resource"
        )

@router.get("/tasks", response_model=List[TodoRead])
def read_tasks(
    user_id: str,
    limit: int = 50,
    offset: int = 0,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Get all tasks for a specific user."""
    validate_user_ownership(current_user, user_id)
    todos = get_todos(session, user_id, limit, offset)
    return todos

@router.post("/tasks", response_model=TodoRead)
def create_task(
    user_id: str,
    todo: TodoCreate,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Create a new task for the user."""
    validate_user_ownership(current_user, user_id)
    db_todo = create_todo(session, todo, user_id)
    return db_todo

@router.get("/tasks/{id}", response_model=TodoRead)
def read_task(
    user_id: str,
    id: str,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Get a specific task for the user."""
    validate_user_ownership(current_user, user_id)
    db_todo = get_todo(session, id, user_id)
    if not db_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return db_todo

@router.put("/tasks/{id}", response_model=TodoRead)
def update_task(
    user_id: str,
    id: str,
    todo_update: TodoUpdate,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Update a specific task for the user."""
    validate_user_ownership(current_user, user_id)
    db_todo = update_todo(session, id, todo_update, user_id)
    if not db_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return db_todo

@router.delete("/tasks/{id}")
def delete_task(
    user_id: str,
    id: str,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Delete a specific task for the user."""
    validate_user_ownership(current_user, user_id)
    success = delete_todo(session, id, user_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return {"message": "Task deleted successfully"}

@router.patch("/tasks/{id}/complete")
def toggle_task_completion(
    user_id: str,
    id: str,
    request: ToggleCompletionRequest,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Toggle completion status of a specific task."""
    validate_user_ownership(current_user, user_id)
    db_todo = toggle_todo_completion(session, id, request.is_completed, user_id)
    if not db_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return db_todo