from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root(BaseModel):
    return {'message':'Welcome to Skill-Swap API'}

    
