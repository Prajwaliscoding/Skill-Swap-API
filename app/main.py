from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'message':'Welcome to PeerUp, a skill_swap API'}

    