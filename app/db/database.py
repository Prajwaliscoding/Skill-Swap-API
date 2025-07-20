from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
load_dotenv()
import os
database_url = os.getenv("DATABASE_URL")
if database_url is None:
    raise ValueError("DATABASE_URL environment variable is not set.")

engine = create_engine(database_url, echo = False)
Session = sessionmaker(bind = engine)
session = Session()

Base = declarative_base()