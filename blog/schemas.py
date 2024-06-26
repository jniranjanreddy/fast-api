from typing import List, Optional
from pydantic import BaseModel

## User related Schemas
class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    # blogs: List[Blog] = []
    class Config():
        from_attributes  = True

class Blog(BaseModel):
    title: str
    body: str
    creator: ShowUser

class ShowBlog(Blog):
    class Config():
        from_attributes  = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None