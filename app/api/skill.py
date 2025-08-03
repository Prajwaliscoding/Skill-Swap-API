# app/api/skill.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.skill import SkillCreate, SkillOut
from app.db.database import get_db
from app.models.user import Skills, Users
from app.crud.skill import create_skill, delete_skill, get_user_skills, get_all_skills, delete_skill
from app.dependencies.auth import get_current_user
from typing import List


router = APIRouter(prefix="/skill", tags=["Skills"])

@router.post("/",response_model= SkillOut)
def add_skill(skill_data: SkillCreate, db: Session =  Depends(get_db), current_user : Users = Depends(get_current_user)):
    return create_skill(skill_data, db, current_user)

@router.get("/", response_model= List[SkillOut])
def list_user_skills(db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    skill = get_user_skills(db, current_user)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not Found")
    return skill

@router.get("/all", response_model= List[SkillOut])
def list_all_skills(db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    return get_all_skills(db)

@router.delete("/delete/{skill_id}")
def remove_skill(skill_id: int, db: Session = Depends(get_db), current_user: Users = Depends (get_current_user)):
    skill = delete_skill(skill_id, db, current_user)

    if not skill:
        raise HTTPException(status_code=404, detail="Skill not Found")

    db.delete(skill)
    db.commit()
    return {"message": "Skill deleted."}