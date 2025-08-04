# app.api.favorites.py

from email import message
from webbrowser import get
from app.dependencies.auth import get_current_user, get_db
from app.models.user import Users, Skills, Favorites
from app.schemas.favorites import FavoriteOut
from app.crud.favorites import add_favorites, user_favorites, delete_favorites
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(prefix = "/favorites", tags= ['Favorites'])

@router.post("/{skill_id}",response_model=FavoriteOut)
def add_favorite(skill_id:int , db: Session = Depends(get_db), current_user : Users = Depends(get_current_user)):
    return add_favorites(skill_id, db, current_user)


@router.get("/",response_model=List[FavoriteOut])
def list_favorites(db: Session = Depends(get_db), current_user : Users = Depends(get_current_user)):
    return user_favorites(db, current_user)


@router.delete("/delete/{skill_id}", response_model=FavoriteOut)
def remove_from_favorites(skill_id:int , db:Session = Depends(get_db), current_user:Users = Depends(get_current_user)):
    return delete_favorites(skill_id,db,current_user)

    
