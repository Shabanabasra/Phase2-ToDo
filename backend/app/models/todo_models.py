from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
import uuid

# User model
class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    name: str

class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship to todos
    todos: List["Todo"] = Relationship(back_populates="owner")

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: uuid.UUID
    created_at: datetime

class UserUpdate(SQLModel):
    name: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None

# Todo model
class TodoBase(SQLModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False
    priority: int = 1  # 1: low, 2: medium, 3: high
    due_date: Optional[datetime] = None

class Todo(TodoBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    owner_id: uuid.UUID = Field(foreign_key="user.id")

    # Relationship to owner
    owner: User = Relationship(back_populates="todos")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class TodoCreate(TodoBase):
    pass

class TodoRead(TodoBase):
    id: uuid.UUID
    owner_id: uuid.UUID
    created_at: datetime
    updated_at: datetime

class TodoUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None
    priority: Optional[int] = None
    due_date: Optional[datetime] = None