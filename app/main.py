# main.py
from fastapi import FastAPI
from app.api import user, auth

app = FastAPI()

@app.get('/')
def root():
    return {'message':'Welcome to PeerUp, a skill_swap API'}

app.include_router(user.router) 

app.include_router(auth.router)  