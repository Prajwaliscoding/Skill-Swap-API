from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.schemas import CreateUser, UserDataOut
from app.crud.crud import create_user
from app.db.database import LocalSession, Base, engine
from app.models import models

router = APIRouter(prefix = "/users", tags = ["Users"])

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()

    
@router.post("/",response_model=UserDataOut)
def register_user(user: CreateUser, db: Session = Depends(get_db)):
    return create_user(db, user)












# bind is the first parameter, so if you just do create_all(engine), SQLAlchemy interprets it as bind=engine.
# You only need to use bind=engine if you're passing additional arguments or for clarity.
# argument and to know which engine are we talking about and connecting to
# create_all(bind=engine)






# What is a "Dependency"?
# In FastAPI, a dependency is a function that provides something your route needs (like a DB session, auth check, etc.). FastAPI automatically calls it, injects the result, and cleans up after it.

# This is done using:

# db: Session = Depends(get_db)
# So when your route is called, FastAPI:

# Calls get_db() before the route runs
# Yields the db session to your function
# After the function runs (success or error), db.close() is called — ensuring the connection is safely closed.
# 🔄 Why use yield?
# yield makes it a generator function, perfect for:
# Giving something to the route (yield db)
# Then doing cleanup after (like db.close())



# "db remains yielded until register_user is done, and once it's done, db closes"
# ✅ YES — that’s 100% correct. You now understand one of the most powerful and clean features of FastAPI.


# 🔹 response_model=UserOut
# This tells FastAPI:

# “After the function runs and returns something, validate and shape the response using the UserOut schema.”
# FastAPI uses the UserOut Pydantic model to:

# Filter the response — so only specific fields are returned (e.g., exclude password)
# Document the response — in the /docs page (Swagger UI)
# Validate output — ensuring correct types and structure


# 🤔 The two look similar but behave very differently:

# ❌ db: Session = get_db()
# You're calling the get_db() function immediately.
# This returns a generator object, not the actual Session.
# So when you do:

# db: Session = get_db()
# You're not getting a usable database session — you're getting this:

# <generator object get_db at 0x...>
# To actually use it, you’d have to do:

# db = next(get_db())  # but this skips the `finally` block (db.close())
# That’s dangerous, and you’re now responsible for closing the session manually.

# ✅ db: Session = Depends(get_db)
# This is how FastAPI’s dependency injection system works.

# You are not calling get_db() yourself.
# You're telling FastAPI:
# “Please call get_db() for me, give me the result, and clean it up when I’m done.”
# So FastAPI:

# Calls get_db()
# Waits for yield db
# Passes db to your route function
# After your route finishes (successfully or not), it resumes the generator and runs db.close() inside the finally
# It manages the entire lifecycle of the dependency.

