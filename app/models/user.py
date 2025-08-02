# models/user.py
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default = True)
    skill = relationship("Skills", back_populates="owner", cascade="all, delete")

class Skills(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable = False)
    skill_type = Column(String, nullable=False)
    user_id = Column (Integer, ForeignKey = "users.id")
    owner = relationship("Users", back_populates= "skill")

