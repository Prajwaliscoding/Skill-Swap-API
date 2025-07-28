# api/user.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import CreateUser, UserDataOut
from app.crud.user import create_user
from app.db.database import LocalSession, Base, engine
from app.models import user

user.Base.metadata.create_all(bind=engine)   

router = APIRouter(prefix = "/users", tags = ["Users"])     

def get_db():
    db = LocalSession()
    try:                           
        yield db
    finally:
        db.close()

    
@router.post("/",response_model=UserDataOut)
def register_user(user: CreateUser, db: Session = Depends(get_db)):
    return create_user(db, user)
