from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True)
    full_name = Column(String(50))
    post = Column(String(20))
    login = Column(String(10))
    password = Column(String(10))
    

DATABASE_URL = "sqlite:///db.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
