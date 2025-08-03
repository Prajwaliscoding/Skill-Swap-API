# app.schemas.skill.py
from pydantic import BaseModel

class SkillCreate(BaseModel):
    name : str
    skill_type : str
    user_id : int

class SkillOut(BaseModel):
    id : int
    name : str
    skill_type : str
    user_id : int

    model_config = {
        "from_attributes": True    
    }



