from sqlalchemy import create_engine
from db.database import Base,engine
from sqlalchemy import Column,String,Integer

class TestUser(Base):
    __tablename__="test_users"
    id=Column(Integer,primary_key=True)
    github_id=Column(Integer,nullable=False)
    name=Column(String,nullable=False)
    # access_token=Column(String,nullable=False)

Base.metadata.create_all(engine)