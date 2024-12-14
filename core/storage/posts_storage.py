from sqlalchemy.sql import text
from sqlalchemy.ext.asyncio import AsyncSession

# from core.models.users.request import UserModel
from ..models.posts.request import PostRequest
from ..models.posts.responses import PostResponses
from .base import BaseStorage

class PostStorage(BaseStorage):
    async def create_posts(self, posts: list[PostRequest]):
        stmt = text("""
            insert into posts (title, content, user_id)
            values(:title, :content, :user_id)
        """)

        async with self.get_session() as session:
            session: AsyncSession
            for post in posts:
                params = post.model_dump(mode="python")
                await session.execute(stmt, params)
                await session.commit()

    async def create_post(self, post: PostRequest) -> list[PostResponses]:
        stmt = text("""
            insert into posts (title, content, user_id)
            values(:title, :content, :user_id)
        """)

        stmt_select = text("""
            select * from posts where user_id = :user_id
        """)

        async with self.get_session() as session:
            session: AsyncSession
            params = post.model_dump(mode="python")
            await session.execute(stmt, params)
            await session.commit()
            data = (await session.execute(stmt_select, params)).fetchall()
            return [PostResponses(
                id=i.id,
                title=i.title,
                content=i.content,
                user_id=i.user_id
            ) for i in data]

    async def get_all_posts(self) -> list[PostRequest]:
        stmt = text("""
            select * from posts
        """)

        async with self.get_session() as session:
            session: AsyncSession
            data = (await session.execute(stmt)).fetchall()
            for post in data:
                print(f"id = {post.id}")
                print(f"title = {post.title}")
                print(f"content = {post.content}")
                print(f"user_id = {post.user_id}")
                print()

            return[PostResponses(
                id=i.id,
                title=i.title,
                content=i.content,
                user_id=i.user_id
            )
            for i in data]

    async def get_post_by_user_id(self, user_id: int) -> list[PostRequest]:
        stmt = text("""
            select * from posts where user_id = :user_id
        """)

        params = {"user_id": user_id}

        async with self.get_session() as session:
            session: AsyncSession
            data = (await session.execute(stmt, params)).fetchall()
            for post in data:
                print(f"id = {post.id}")
                print(f"title = {post.title}")
                print(f"content = {post.content}")
                print(f"user_id = {post.user_id}")
                print()

            return[PostResponses(
                id=i.id,
                title=i.title,
                content=i.content,
                user_id=i.user_id
            )
            for i in data]

    async def delete_post_by_id(self, post_id: int) -> list[PostRequest]:
        stmt = text("""
            delete from posts
            where id = :id
        """)

        stmt_select = text("""
            select user_id from posts where id = :id
        """)

        params = {"id": post_id}

        async with self.get_session() as session:
            session: AsyncSession
            data = (await session.execute(stmt_select, params)).fetchone()
            await session.execute(stmt, params)
            await session.commit()
            return await self.get_post_by_user_id(data.user_id)

    async def delete_post_by_user_id(self, user_id: int) -> list[PostRequest]:
        stmt = text("""
            delete from posts
            where user_id = :user_id
        """)

        params = {"user_id": user_id}

        async with self.get_session() as session:
            session: AsyncSession
            await session.execute(stmt, params)
            await session.commit()
            return await self.get_all_posts()

    async def update_content(self, post: PostResponses) -> list[PostResponses]:
        stmt = text("""
            update posts set content = :content where id = :id
        """)

        params = post.model_dump(mode="python")

        async with self.get_session() as session:
            session: AsyncSession
            await session.execute(stmt, params)
            await session.commit()
            return await self.get_post_by_user_id(post.user_id)
