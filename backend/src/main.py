# -------------------------------
# Load environment variables first
# -------------------------------
from dotenv import load_dotenv
load_dotenv()  # 👈 Make sure this is called before using DATABASE_URL

# -------------------------------
# Import FastAPI and middleware
# -------------------------------
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# -------------------------------
# Import routers and database
# -------------------------------
from .api.auth import router as auth_router
from .api.todos import router as todos_router
from .database.session import engine
from .models.user import User
from .models.todo import Todo
from sqlmodel import SQLModel

# -------------------------------
# Initialize FastAPI app
# -------------------------------
app = FastAPI(
    title="Todo Full-Stack Web Application API",
    description="API for managing user todos with authentication and user isolation",
    version="1.0.0"
)

# -------------------------------
# Add CORS middleware
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Include routers
# -------------------------------
app.include_router(auth_router)
app.include_router(todos_router)

# -------------------------------
# Startup event: create tables
# -------------------------------
@app.on_event("startup")  # type: ignore[method-assign]
def on_startup():
    # Create all database tables
    SQLModel.metadata.create_all(bind=engine)

# -------------------------------
# Root & Health check endpoints
# -------------------------------
@app.get("/")
def read_root():
    return {"message": "Todo API is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
