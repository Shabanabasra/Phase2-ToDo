"""
Simple test script to verify the API functionality
"""

import requests
import json
import time

BASE_URL = "http://localhost:8000"

def test_api():
    print("Testing Todo API...")

    # Test registration
    print("\n1. Testing user registration...")
    register_data = {
        "name": "Test User",
        "email": f"test{int(time.time())}@example.com",
        "password": "securepassword123"
    }

    response = requests.post(f"{BASE_URL}/auth/register", json=register_data)
    if response.status_code == 200:
        print("✓ Registration successful")
        user_data = response.json()
        print(f"  User ID: {user_data['id']}")
        email = register_data['email']
    else:
        print(f"✗ Registration failed: {response.text}")
        return

    # Test login
    print("\n2. Testing user login...")
    login_data = {
        "email": email,
        "password": "securepassword123"
    }

    response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
    if response.status_code == 200:
        print("✓ Login successful")
        token_data = response.json()
        access_token = token_data['access_token']
        print(f"  Access token received")
    else:
        print(f"✗ Login failed: {response.text}")
        return

    # Set up authorization header
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Test getting user details
    print("\n3. Testing getting user details...")
    response = requests.get(f"{BASE_URL}/users/me", headers=headers)
    if response.status_code == 200:
        print("✓ User details retrieved successfully")
        user_info = response.json()
        print(f"  User: {user_info['name']} ({user_info['email']})")
    else:
        print(f"✗ Failed to get user details: {response.text}")

    # Test creating a todo
    print("\n4. Testing creating a todo...")
    todo_data = {
        "title": "Test Todo",
        "description": "This is a test todo item",
        "priority": 2
    }

    response = requests.post(f"{BASE_URL}/todos/", json=todo_data, headers=headers)
    if response.status_code == 200:
        print("✓ Todo created successfully")
        todo = response.json()
        todo_id = todo['id']
        print(f"  Todo ID: {todo_id}")
        print(f"  Title: {todo['title']}")
    else:
        print(f"✗ Failed to create todo: {response.text}")
        return

    # Test getting all todos
    print("\n5. Testing getting all todos...")
    response = requests.get(f"{BASE_URL}/todos/", headers=headers)
    if response.status_code == 200:
        print("✓ Todos retrieved successfully")
        todos = response.json()
        print(f"  Number of todos: {len(todos)}")
    else:
        print(f"✗ Failed to get todos: {response.text}")

    # Test getting a specific todo
    print(f"\n6. Testing getting specific todo (ID: {todo_id[:8]}...)...")
    response = requests.get(f"{BASE_URL}/todos/{todo_id}", headers=headers)
    if response.status_code == 200:
        print("✓ Specific todo retrieved successfully")
        todo = response.json()
        print(f"  Title: {todo['title']}")
    else:
        print(f"✗ Failed to get specific todo: {response.text}")

    # Test updating a todo
    print(f"\n7. Testing updating todo (ID: {todo_id[:8]}...)...")
    update_data = {
        "title": "Updated Test Todo",
        "is_completed": True
    }

    response = requests.put(f"{BASE_URL}/todos/{todo_id}", json=update_data, headers=headers)
    if response.status_code == 200:
        print("✓ Todo updated successfully")
        updated_todo = response.json()
        print(f"  New title: {updated_todo['title']}")
        print(f"  Completed: {updated_todo['is_completed']}")
    else:
        print(f"✗ Failed to update todo: {response.text}")

    # Test deleting a todo
    print(f"\n8. Testing deleting todo (ID: {todo_id[:8]}...)...")
    response = requests.delete(f"{BASE_URL}/todos/{todo_id}", headers=headers)
    if response.status_code == 200:
        print("✓ Todo deleted successfully")
    else:
        print(f"✗ Failed to delete todo: {response.text}")

    print("\n✓ All tests completed successfully!")

if __name__ == "__main__":
    test_api()