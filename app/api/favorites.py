# app.api.favorites.py

from app.dependencies.auth import get_current_user, get_db
from app.models.user import Users, Skills, Favorites
from app.schemas.favorites import FavoriteOut
from app.crud.favorites import add_favorites
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(prefix = "/favorites", tags= ['Favorites'])

@router.post("/{skill_id}",response_model=FavoriteOut)
def add_favorite(skill_id:int , db: Session = Depends(get_db), current_user : Users = Depends(get_current_user)):
    return add_favorites(skill_id, db, current_user)