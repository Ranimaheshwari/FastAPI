# Pydantic model which is a response model, we call it schema.
from lib2to3.pytree import Base
from typing import List, Optional
from pydantic import BaseModel


class BlogBase(BaseModel):
    title :str
    body : str


class Blog(BlogBase):
    title :str
    body : str
    class Config():
        orm_mode = True


# class ShowBlog(Blog):
#     class Config():
#         orm_mode = True

# OR we can do this as well


class User(BaseModel):
    name : str
    email : str
    password :str

class ShowUSer(BaseModel):
    name: str
    email: str
    blogs : List[Blog]
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title : str
    body: str
    creator: ShowUSer
    class Config():
        orm_mode = True

class Login(BaseModel):
    username : str
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None