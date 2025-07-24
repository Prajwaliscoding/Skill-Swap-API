# crud.py
from sqlalchemy.orm import Session       
from app.models.models import Users
from app.schemas.schemas import CreateUser
from passlib.context import CryptContext  # type: ignore   

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


