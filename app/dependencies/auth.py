from fastapi import Depends, HTTPException, status 
from fastapi.security import APIKeyHeader 
from jose import JWTError, jwt # type: ignore   
from sqlalchemy.orm import Session
from app.core.config import settings
from app.db.database import get_db
from app.models.user import Users

oauth2_scheme = APIKeyHeader(name="Authorization")      

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate credentials",headers={"WWW-Authenticate": "Bearer"})

    if token.startswith("Bearer "):
        token = token.split("Bearer ")[1]

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email_value = payload.get("sub")
        if email_value is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(Users).filter(Users.email == email_value).first()
    if user is None:
        raise credentials_exception

    return user
