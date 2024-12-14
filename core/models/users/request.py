from pydantic import BaseModel, EmailStr
from typing import Optional

class UserRequest(BaseModel):
    username: str
    email: EmailStr
    password: Optional[str] = None

