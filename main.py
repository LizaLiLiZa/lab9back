"""The main file"""
import uvicorn
from fastapi import FastAPI
from core.migration.create_table import create_table

from core.models.users.request import UserRequest
from core.storage import users_storage
from core.models.posts.request import PostRequest
from core.storage import posts_storage

user1 = UserRequest(username="Lola", email="milly.ili000@gmail.com", password="88005553535")
user2 = UserRequest(username="Mila", email="milly@gmail.com", password="8001253535")
user3 = UserRequest(username="Jhon", email="Jhon.Jhon@gmail.com", password="wer05553535")

all_users = [user1, user2, user3]

post1 = PostRequest(title="С новым годом!", content="Всех с новым годом!!!", user_id=1)
post2 = PostRequest(title="С новым счастьем!", content="Всех с новым годом!!!", user_id=1)
post3 = PostRequest(title="С новым годом!", content="Всех с новым годом!!!", user_id=3)

all_post = [post1, post2, post3]

from config import Config
from core.api import router as api_router

app = FastAPI()

app.include_router(api_router)

if __name__ == '__main__':
    import asyncio
    # asyncio.run(create_table())
    # asyncio.run(users_storage.create_users(all_users))
    # asyncio.run(users_storage.get_all_users())
    # asyncio.run(posts_storage.create_posts(all_post))
    # asyncio.run(posts_storage.get_all_posts())
    # asyncio.run(posts_storage.get_post_by_user_id(1))
    # asyncio.run(users_storage.get_user_by_id(1))
    # asyncio.run(users_storage.update_email("lalalend@mail.str", 1))
    # asyncio.run(posts_storage.delete_post_by_id(1))
    # asyncio.run(posts_storage.delete_post_by_user_id(1))
    # asyncio.run(users_storage.delete_user(3))
    # uvicorn.run('main:app', host = str(Config.host), port = Config.port, reload=True)
