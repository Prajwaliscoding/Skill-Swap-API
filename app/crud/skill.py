from app.models.user import Skills, Users
from sqlalchemy.orm import Session
from app.schemas.skill import SkillCreate


def create_skill(skill_data: SkillCreate, db: Session,current_user: Users):
    db_skill = Skills(
        name = skill_data.name, 
        skill_type = skill_data.skill_type,
        user_id = current_user.id )      
    
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

def get_user_skills(db: Session, current_user: Users):
    return db.query(Skills).filter(Skills.user_id == current_user.id).all()

def get_all_skills(db: Session):
    return db.query(Skills).all()

def delete_skill(skill_id:int, db:Session, current_user: Users):
    return db.query(Skills).filter(Skills.id == skill_id, Skills.user_id == current_user.id).first()   # Match by skill ID, Ensure the skill belongs to logged-in user

