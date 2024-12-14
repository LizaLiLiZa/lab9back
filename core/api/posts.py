from fastapi import APIRouter
from pydantic import EmailStr

from ..storage import posts_storage

from ..models.posts.request import PostRequest
from ..models.posts.responses import PostResponses

router = APIRouter(tags=["Post"])

@router.post("/post")
async def create_post(post: PostRequest) -> list[PostResponses]:
    return await posts_storage.create_post(post)

@router.get("/posts")
async def get_posts() -> list[PostResponses]:
    return await posts_storage.get_all_posts()

@router.get("/post")
async def get_post(user_id: int) -> list[PostResponses]:
    return await posts_storage.get_post_by_user_id(user_id)

@router.put("/post")
async def update_content(post: PostResponses) -> list[PostResponses]:
    return await posts_storage.update_content(post)

@router.delete("/post")
async def delete_post(post_id: int):
    return await posts_storage.delete_post_by_id(post_id)
