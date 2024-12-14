from pydantic import BaseModel

class PostResponses(BaseModel):
    id: int
    title: str
    content: str
    user_id: int
