# schemas.py
from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):     # for validating the data entered to store user in database.
    name: str
    email: EmailStr
    password: str


class UserDataOut(BaseModel):    # for validating the data given to the user as response
    id: int
    name: str
    email: EmailStr
    is_active: bool

    model_config = {
        "from_attributes": True    
    }



# 📦 Context: We're using Pydantic v2
# In Pydantic v2, the configuration style changed. Now we use:

# model_config = {
#     "from_attributes": True
# }


# The data is stored in the database.
# When you query the database, you get SQLAlchemy objects.
# But FastAPI can't return those objects as JSON directly, so you use a Pydantic model with
# model_config = {"from_attributes": True} to convert those SQLAlchemy objects into JSON for the response.