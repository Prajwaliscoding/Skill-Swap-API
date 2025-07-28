from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserLogin
from app.schemas.token import Token
from app.crud.user import authenticate_user
from app.core.security import create_access_token
from app.api.user import get_db

router = APIRouter( prefix = "/auth", tags = ["Authentication"] )

@router.post("/login",response_model= Token)
def login(user_login: UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(db, user_login.email, user_login.password)
    if not user:
        raise HTTPException(status_code= 404, detail="Invalid email or password")
    
    access_token = create_access_token(data={"sub": user.email})     
    return {"access_token" : access_token, "access_type": "bearer"}



