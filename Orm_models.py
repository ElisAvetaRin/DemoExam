from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import bcrypt

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True)
    full_name = Column(String(120))
    post = Column(String(200))
    login = Column(String(10))
    password = Column(String(10))

    def hash_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def save(self):
        SessionLocal.add(self)
        SessionLocal.commit()

DATABASE_URL = "sqlite:///db.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
