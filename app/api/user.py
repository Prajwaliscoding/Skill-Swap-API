# user.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import CreateUser, UserDataOut, UserUpdate
from app.crud.user import create_user, update_user
from app.db.database import get_db
from app.models.user import Users
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserDataOut)
def register_user(user: CreateUser, db: Session = Depends(get_db)):  
    return create_user(db, user)

@router.get("/me", response_model=UserDataOut)
def read_users_me(current_user: Users = Depends(get_current_user)):
    return current_user

@router.put("/me",response_model=UserDataOut)
def update_profile(updates: UserUpdate, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    return update_user(db, current_user, updates)
    