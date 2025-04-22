from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class Space(BaseModel):
    title: str
    description: str

class Page(BaseModel):
    title: str
    content: str
    space_id: str
