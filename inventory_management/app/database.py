from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://megha_2olk_user:At2l4ZXepu3O8VS6GRgCzlRZpOlxh9Dh@dpg-cs18s1ggph6c73ai3t00-a.oregon-postgres.render.com/megha_2olk" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
