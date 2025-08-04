from fastapi import APIRouter, HTTPException
from app.models import User
from app.services.user_service import UserService

router = APIRouter()
service = UserService()

# Create a new user
@router.post("/users/")
def create_user(user: User):
    return service.create_user(user)

# Get a user by ID
@router.get("/users/{user_id}")
def get_user(user_id: int):
    user = service.get_user(user_id)
    if not user or "error" in user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# ✅ Update user by ID
@router.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    updated_user = service.update_user(user_id, user)
    if "error" in updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

# Delete user by ID
@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    result = service.delete_user(user_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail="User not found")
    return result

# List all users
@router.get("/users/")
def list_users():
    return service.get_users()
