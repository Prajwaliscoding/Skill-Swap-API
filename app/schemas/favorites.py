# app/schemas/favorites.py
from pydantic import BaseModel

class FavoriteOut(BaseModel):
    id : int
    user_id : int
    skill_id : int

    model_config = {
        "from_attributes" : True
    }