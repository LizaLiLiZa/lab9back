from typing import Optional
from pydantic import BaseModel

class PostRequest(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    user_id: int
