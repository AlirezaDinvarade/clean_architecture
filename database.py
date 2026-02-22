from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from redis import Redis
import os

load_dotenv()
postgres_user = os.getenv("POSTGRES_USER")
postgres_password = os.getenv("POSTGRES_PASSWORD")
postgres_database = os.getenv("POSTGRES_DB")


DATABASE_URL = f"postgresql://{postgres_user}:{postgres_password}@localhost:5432/{postgres_database}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_postgres_session():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()


def get_redis_session():
    redis = Redis(host='localhost', port=6379, db=0, password=os.getenv("REDIS_PASSWORD"))
    try:
        yield redis
    finally:
        redis.close()