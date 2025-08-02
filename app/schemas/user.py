# schemas/user.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Annotated

class CreateUser(BaseModel):     
    name: str
    email: EmailStr
    password: str


class UserDataOut(BaseModel):    
    id: int
    name: str
    email: EmailStr
    is_active: bool

    model_config = {
        "from_attributes": True    
    }

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    name:Optional[str]= None
    bio: Annotated[Optional[str], Field(default= None, max_length = 200, title ="Bio of the User", description = "Give your bio in 200 characters.")]