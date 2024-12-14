from database import Session
from .users_storage import UserStorage
from .posts_storage import PostStorage
from .base import BaseStorage

base_storage = BaseStorage(Session)
users_storage = UserStorage(Session)
posts_storage = PostStorage(Session)
