from passlib.context import CryptContext
# You're importing CryptContext from Passlib, a library for secure password hashing.
# It manages which hashing algorithm to use (like bcrypt), and how to verify hashed passwords.
# Why: Never store plain text passwords — always store hashed ones.

from datetime import datetime, timedelta, timezone
# datetime → Gets the current time.
# timedelta → Lets you add/subtract time (e.g., token expires in 30 minutes).
# timezone → Used to make the time timezone-aware, usually UTC.
# Why: JWTs need exp (expiration) times that are UTC-aware.

from jose import jwt
# This imports the jwt module from the python-jose package.
# Used to create and verify JWT tokens.
# JWT (JSON Web Token): A compact, signed token that proves the user is logged in.

from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

secret_key = os.getenv("SECRET_KEY","None")
if secret_key == "None":
    raise ValueError("SECRET_KEY environment variable not set")

algorithm = os.getenv("ALGORITHM", "HS256")
ACCESS_TIME_EXPIRE_MINUTES = 30       
# Sets a default expiration time for access tokens.     
# Convention: Constants should be UPPER_CASE: ACCESS_TOKEN_EXPIRE_MINUTES.


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# You create a CryptContext that:
# Uses bcrypt (a slow, secure hashing algorithm).
# Treats older algorithms as deprecated if you switch later.
# bcrypt adds salt, making password hashes unique and secure.
# NEVER hash passwords manually with SHA256 or MD5 — use this.

def hash_password(password: str) -> str:
    return pwd_context.hash(password)
# This function:
# Takes a plain password ("mypassword123").
# Returns a bcrypt hash, e.g., $2b$12$Z0vEzTz...
# Used when a user registers.

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
# This function:
# Takes the password the user typed during login.
# Compares it with the hashed password from the database.
# Returns True if they match.
# Passlib handles salting + secure comparison internally.

def create_access_token(data: dict, expires_delta: Optional[timedelta]=None):
# 3 parts of token(2nd part is claim a.k.a data or dict), this is required.
# Function to create and return a JWT.
# data: dict → the information you want to store in the token (e.g., {"sub": user_id}).
# expires_delta: Optional[timedelta] → custom expiry time. If None, use default.
    to_encode = data.copy()
    # hamile tala yo data ma arko kura halxau("exp":expire) tesaile original wala change nahos vanera arko dummy banako.
    # to_encode = data ; copy() function use nagarera yo gareko vaye-> you're just creating a new name for the same object. So modifying to_encode will also change data, which can cause bugs.

    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TIME_EXPIRE_MINUTES))
    # sets when the token will expire:
    # If expires_delta is passed, use it.
    # Otherwise, use 30 minutes by default.
    # datetime.now(timezone.utc) ensures you're using UTC, which is required by the JWT spec.

    # datetime.now(timezone.utc) + (None or timedelta(minutes=30))
    # Since None is falsy, it moves to the second option:

    to_encode.update({"exp": expire})
    # hamile dictionary ma yo key-value pair add gareko, merge gareko
    # JWT requires an exp (expiration) field to know when the token becomes invalid.
    # This line adds it to the token payload.

    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm) # yo order ma pass gareko xa(positional arguments). order birsiye can do-> encoded_jwt = jwt.encode(payload = to_encode, key = secret_key, algorithm=algorithm)
    # Creates (signs) the token using:
    # The payload (to_encode)
    # The secret key (secret_key)
    # The algorithm (HS256)

    return encoded_jwt
    # Returns the final JWT token string, ready to send to the frontend.
