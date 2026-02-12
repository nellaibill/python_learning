from sqlalchemy import Column,Integer,String
from app.database import Base

class UserModel(Base):
    __tablename__ ="users1"
    
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    email = Column(String(100))
    
    