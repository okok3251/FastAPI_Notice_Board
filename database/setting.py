from pydantic_settings import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    DATABASE : Optional[str] = None # python 3.10 버전 이후부터는 str | None = None으로 가능하다 (똑같은 말임)

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), '../initial_setting.env')


settings = Settings()

