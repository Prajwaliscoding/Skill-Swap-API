# app.crud.favorites.py

from app.models.user import Users, Favorites
from sqlalchemy.orm import Session

def add_favorites(skill_id:int, db: Session, current_user: Users):
    fav = Favorites(user_id = current_user.id, skill_id = skill_id)

    db.add(fav)
    db.commit()
    db.refresh(fav)
    return fav

def user_favorites(db: Session, current_user: Users):
    return db.query(Favorites).filter(Favorites.user_id == current_user.id).all()