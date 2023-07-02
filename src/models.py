```python
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from src.database import SessionLocal, engine

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    content = Column(String)
    timestamp = Column(DateTime)

Base.metadata.create_all(bind=engine)
```