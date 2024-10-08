from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://dastask7_user:uGT2aMJmlvbjQCLbajsOYwKTG1B97l0e@dpg-crul5c3tq21c738kod50-a.singapore-postgres.render.com/dastask7"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
