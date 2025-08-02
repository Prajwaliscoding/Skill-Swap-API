from app.models.user import Skills, Users
from sqlalchemy.orm import Session
from app.schemas.skill import SkillCreate


def create_skill(skill_data: SkillCreate, db: Session,current_user: Users):
    db_skill = Skills(
        name = skill_data.name, 
        skill_type = skill_data.skill_type,
        user_id = current_user.id )      #  Link skill to the logged-in user
    
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

