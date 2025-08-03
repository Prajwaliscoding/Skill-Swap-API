# models/user.py
from turtle import back
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
    favorites = relationship("Favorites", back_populates= "favorites_users", cascade = "all, delete")

class Skills(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable = False)
    skill_type = Column(String, nullable=False)
    user_id = Column (Integer, ForeignKey("users.id"))

    owner = relationship("Users", back_populates= "skill")
    favorites = relationship("Favorites",back_populates="favorites_skills", cascade="all,delete")

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key= True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete= "CASCADE"))  #  You don’t need to manually delete favorites when deleting a user.
    skill_id = Column(Integer, ForeignKey("skills.id", ondelete= "CASCADE"))

    favorites_users = relationship("Users", back_populates="favorites")
    favorites_skills = relationship("Skills")