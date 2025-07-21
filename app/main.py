from fastapi import FastAPI
from app.api import api
app = FastAPI()

@app.get('/')
def root():
    return {'message':'Welcome to PeerUp, a skill_swap API'}

app.include_router(api.router)

    