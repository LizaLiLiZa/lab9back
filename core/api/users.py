from fastapi import APIRouter
from pydantic import EmailStr

from ..storage import users_storage

from ..models.users.request import UserRequest
from ..models.users.responses import UserResponse

router = APIRouter(tags=["User"])

@router.post("/user")
async def create_user(user: UserRequest) -> UserResponse:
    return await users_storage.create_user(user)

@router.get("/users")
async def get_users() -> list[UserResponse]:
    return await users_storage.get_all_users()

@router.get("/user")
async def get_user_by_id(user_id: int) -> UserResponse:
    return await users_storage.get_user_by_id(user_id)

@router.put("/user/email")
async def update_email(email: EmailStr, user_id: int) -> UserResponse:
    return await users_storage.update_email(email, user_id)

@router.delete("/user")
async def delete_user(user_id: int):
    return await users_storage.delete_user(user_id)
