# crud/user.py
from sqlalchemy.orm import Session       
from app.models.user import Users
from app.schemas.user import CreateUser
from passlib.context import CryptContext  # type: ignore  
from app.core.security import verify_password 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 

def get_password_hash(password):
    return pwd_context.hash(password)    

def create_user(db:Session,  user:CreateUser):     
    hashed_pw = get_password_hash(user.password)
    db_user = Users(name=user.name, email=user.email, hashed_password=hashed_pw) 
    db.add(db_user)
    db.commit()     
    db.refresh(db_user)  
    return db_user

def authenticate_user(db:Session, email:str, password:str):
    user = db.query(Users).filter(Users.email == email).first()
    if not user:
        return None
    if not verify_password(password,str(user.hashed_password)):
        return None
    return user