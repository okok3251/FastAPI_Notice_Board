from sqlalchemy import create_engine # 데이터 베이스와 연결할 수 있는 엔진을 생성
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .setting import settings # 아까 정의한 setting 객체를 가져온다.


engine = create_engine(
    settings.DATABASE
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()
