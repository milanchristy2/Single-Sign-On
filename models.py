from database import Base,engine
from sqlalchemy import Column,Integer,String

class User(Base):
    __tablename__ = 'test_users'
    id=Column(Integer,primary_key=True)
    github_id=Column(Integer)
    name=Column(String,nullable=False,unique=True)

Base.metadata.create_all(engine)