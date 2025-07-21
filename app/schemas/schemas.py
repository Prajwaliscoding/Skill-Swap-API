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

    model_config = {
        "from_attributes": True
    }
    


# 📦 Context: You're using Pydantic v2
# In Pydantic v1, we used:

# class Config:
#     orm_mode = True
# In Pydantic v2, the configuration style changed. Now you use:

# model_config = {
#     "from_attributes": True
# }