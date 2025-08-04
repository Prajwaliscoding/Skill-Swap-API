# app.crud.favorites.py

from fastapi import HTTPException
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

def delete_favorites(skill_id, db, current_user):
    fav = db.query(Favorites).filter(Favorites.skill_id == skill_id, Favorites.user_id == current_user.id).first()

    if not fav:
        raise HTTPException(status_code= 404 , detail="Favorite not found.")

    db.delete(fav)
    db.commit()
    return fav