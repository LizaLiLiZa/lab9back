from sqlalchemy.sql import text
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import EmailStr
from fastapi import HTTPException

from ..models.users.request import UserRequest
from ..models.users.responses import UserResponse
from .base import BaseStorage

class UserStorage(BaseStorage):
    async def create_users(self, users: list[UserRequest]):
        stmt = text("""
            insert into users (username, email, password)
            values (:username, :email, :password)
        """)

        async with self.get_session() as session:
            session: AsyncSession
            for user in users:
                params = user.model_dump(mode="python")
                await session.execute(stmt, params)
                await session.commit()

    async def create_user(self, user: UserRequest):
        stmt = text("""
            insert into users (username, email, password)
            values (:username, :email, :password)
        """)

        stmt_select = text("""
            select * from users where email = :email
        """)

        async with self.get_session() as session:
            session: AsyncSession
            params = user.model_dump(mode="python")
            try:
                await session.execute(stmt, params)
                await session.commit()
                data = (await session.execute(stmt_select, params)).fetchone()
                print(data)
                return UserResponse(
                    id=data.id,
                    username=data.username,
                    email=data.email,
                    password=data.password
                )
            except Exception as exc:
                raise HTTPException(status_code=422, detail="Пользователь с такими даннмыми уже существует!") from exc

    async def get_all_users(self) -> list[UserResponse]:
        stmt = text("""
            select * from users
        """)

        async with self.get_session() as session:
            session: AsyncSession
            data = (await session.execute(stmt)).fetchall()
            for i in data:
                print(f"id = {i.id}")
                print(f"username = {i.username}")
                print(f"email = {i.email}")
                print(f"password = {i.password}")
                print()
            return[UserResponse(
                id=i.id,
                username=i.username,
                email=i.email,
                password=i.password
            )for i in data]

    async def get_user_by_id(self, user_id: int) -> UserResponse:
        stmt = text("""
            select * from users
            where id = :id
        """)

        params = {"id": user_id}

        async with self.get_session() as session:
            session: AsyncSession
            data = (await session.execute(stmt, params)).fetchone()
            print(data)
            return UserResponse(
                id=data.id,
                username=data.username,
                email=data.email,
                password=data.password
            )

    async def update_email(self, email: EmailStr, user_id: int):
        stmt = text("""
            update users set email = :email
            where id = :id
        """)

        params = {
            "email": email,
            "id": user_id
        }

        async with self.get_session() as session:
            session: AsyncSession
            try:
                await session.execute(stmt, params)
                await session.commit()
                return await self.get_user_by_id(user_id)
            except Exception as exc:
                raise HTTPException(status_code=422, detail="Пользователь с такими даннмыми уже существует!") from exc

    async def delete_user(self, user_id: int) -> bool:
        from ..storage import posts_storage
        stmt = text("""
            delete from users where id = :id
        """)

        params = {"id": user_id}

        async with self.get_session() as session:
            session: AsyncSession
            await posts_storage.delete_post_by_user_id(user_id)
            await session.execute(stmt, params)
            await session.commit()
            return True
