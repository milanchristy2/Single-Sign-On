from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import os

load_dotenv()

DATABASE_URL=os.getenv("DATABASE_URL")


engine=create_engine(DATABASE_URL)
Session=sessionmaker(bind=engine)
Base=declarative_base()

def get_db():
    db=Session()
    try:
        yield db
    finally:
        db.close()

