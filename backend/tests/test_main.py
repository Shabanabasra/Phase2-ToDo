import pytest
from fastapi.testclient import TestClient
from src.main import app
from sqlmodel import SQLModel, create_engine
from src.database.session import get_session
from unittest.mock import dependency

# Test client
client = TestClient(app)

def test_read_root():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Todo API is running!"}

def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_cors_middleware():
    """Test that CORS headers are present."""
    response = client.get("/")
    assert "access-control-allow-origin" in response.headers