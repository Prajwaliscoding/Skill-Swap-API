# SkillSwap API (PeerUp)
A FastAPI-based platform where users can list their skills, find others, mark favorites, and connect.

## Features
- User registration & JWT authentication
- Skill creation, listing, search
- Mark skills as favorites
- Protected routes for personal data
- PostgreSQL database integration
- Dockerized for easy deployment

## Tech Stack
- **Backend:** Python, FastAPI, SQLAlchemy
- **Database:** PostgreSQL
- **Auth:** JWT
- **Deployment:** Docker + Render

## Getting Started (Local Development)

### 1. Clone the repository
```bash
git clone https://github.com/Prajwaliscoding/Skill-Swap-API.git 
cd Skill-Swap-API
```

### 2. Create and activate virtual environment
bash
```
python -m venv myvenv
source myvenv/bin/activate  # On Windows use: myvenv\Scripts\activate
```

### 3. Install dependencies
bash 
```
pip install -r requirements.txt
```

### 4. Set up .env

bash 
```
cp .env.example .env
```

### 5. Edit .env
.env
```
DATABASE_URL=postgresql://username:password@localhost:5432/your_db_name
SECRET_KEY=replace_with_strong_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 6. Run the app
```bash
uvicorn app.main:app --reload
```
Visit: http://127.0.0.1:8000/docs



## Running with Docker

