from fastapi import FastAPI
import uvicorn 

from fastapi.middleware.cors import CORSMiddleware
import database.models
from domain.combined_router import combined_router

def include_router(app):
    app.include_router(combined_router)


def start_application(): 
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    ) # 통신하기 위한 미들웨어


    # # database.modles.Base.metadata.drop_all(bind=setting.database.engine) # 테이블 삭제
    # database.models.Base.metadata.create_all(bind=database.database.engine) # 테이블 생성

    include_router(app) 
    return app 

app = start_application() 





if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True) # python main.py로 실행 가능
