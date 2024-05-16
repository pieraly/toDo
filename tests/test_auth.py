
from fastapi.testclient import TestClient
from main import app 
from unittest.mock import patch

@patch("firebase_admin.auth.create_user")
def test_signup(mock_create_user):
    client = TestClient(app)

    user_data = {"email": "test@example.com", "password": "password"}

    mock_create_user.return_value.uid = "mocked_uid"

    response = client.post("/auth/signup", json=user_data)

    assert response.status_code == 200

    mock_create_user.assert_called_once_with(email=user_data["email"], password=user_data["password"])

    print(f"User data: {user_data}")
    print(f"Mock create_user arguments: {mock_create_user.call_args}")

@patch("database.firebase.authTodo.sign_in_with_email_and_password")
def test_login(mock_sign_in):
    client = TestClient(app)

    login_data = {"username": "test@example.com", "password": "testpassword"}

    mock_sign_in.return_value = {"idToken": "mocked_token"}

    response = client.post("/auth/login", data=login_data)

    assert response.status_code == 200
    assert response.json() == {"access_token": "mocked_token", "token_type": "bearer"}

    mock_sign_in.assert_called_once_with(email="test@example.com", password="testpassword")