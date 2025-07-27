from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt

from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

secret_key = os.getenv("SECRET_KEY","None")
if secret_key == "None":
    raise ValueError("SECRET_KEY environment variable not set")

algorithm = os.getenv("ALGORITHM", "HS256")
ACCESS_TIME_EXPIRE_MINUTES = 30       

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta]=None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TIME_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm) 
    return encoded_jwt
