# app/api/skill.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.skill import SkillCreate, SkillOut
from app.db.database import get_db
from app.models.user import Skills, Users
from app.crud.skill import create_skill
from app.dependencies.auth import get_current_user


router = APIRouter(prefix="/skill", tags=["Skills"])

@router.post("/",response_model= SkillOut)
def add_skill(skill_data: SkillCreate, db: Session =  Depends(get_db), current_user : Users = Depends(get_current_user)):
    return create_skill(skill_data, db, current_user)