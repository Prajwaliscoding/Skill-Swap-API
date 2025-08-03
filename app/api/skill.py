# app/api/skill.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.skill import SkillCreate, SkillOut
from app.db.database import get_db
from app.models.user import Skills, Users
from app.crud.skill import create_skill, get_user_skills, get_all_skills
from app.dependencies.auth import get_current_user
from typing import List


router = APIRouter(prefix="/skill", tags=["Skills"])

@router.post("/",response_model= SkillOut)
def add_skill(skill_data: SkillCreate, db: Session =  Depends(get_db), current_user : Users = Depends(get_current_user)):
    return create_skill(skill_data, db, current_user)

@router.get("/", response_model= List[SkillOut])
def list_user_skills(db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    return get_user_skills(db, current_user)

@router.get("/all", response_model= List[SkillOut])
def list_all_skills(db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    return get_all_skills(db)
