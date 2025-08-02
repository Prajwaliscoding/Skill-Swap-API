from pydantic import BaseModel, Field
from typing import Literal, Annotated

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



