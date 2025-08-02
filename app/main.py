# main.py
from fastapi import FastAPI
from app.api import user, auth, skill

from app.models import user as user_model
from app.db.database import Base, engine  

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
def root():
    return {'message':'Welcome to PeerUp, a skill_swap API'}

app.include_router(user.router) 

app.include_router(auth.router) 

app.include_router(skill.router)
