from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserDataOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool

    class Config():
        orm_mode = True
