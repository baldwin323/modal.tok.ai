```python
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class Subscriber(Base):
    __tablename__ = "subscribers"

    subscriber_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    name = Column(String)
    email = Column(String, unique=True, index=True)
    subscribed_date = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    preferences = Column(String)

    user = relationship("User", back_populates="subscribers")

    def __init__(self, user_id, name, email, preferences):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.preferences = preferences

    def __repr__(self):
        return f"<Subscriber {self.name}>"
```