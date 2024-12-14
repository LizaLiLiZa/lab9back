from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy import MetaData
from database import engine

metadata = MetaData()

users = Table('users', metadata,
              Column('id', Integer(), primary_key=True, autoincrement='auto'),
              Column('username', String(200), nullable=False, unique=True),
              Column('email', String(200), nullable=False, unique=True),
              Column('password', String(15))
        )

posts = Table('posts', metadata,
            Column('id', Integer(), primary_key=True, autoincrement='auto'),
            Column('title', String(200)),
            Column('content', String(200)),
            Column('user_id', Integer(), ForeignKey("users.id"))
        )

async def create_table():
    async with engine.begin() as conn:
        print(metadata.tables.keys())
        await conn.run_sync(metadata.create_all)
