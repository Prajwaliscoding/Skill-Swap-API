# schemas/user.py
from pydantic import BaseModel, EmailStr
from typing import Optional

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
    bio: Optional[str]= None