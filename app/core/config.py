import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Setting(BaseSettings):

    PG_USER: str
    PG_DB: str
    PG_HOST: str
    PG_PASS: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0

    ROOM_CODE_LENGTH: int = 6
    CACHE_TTL: int = 86400  #

    @property
    def ASYNC_DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.PG_USER}:{self.PG_PASS}@{self.PG_HOST}/{self.PG_DB}"

    @property
    def DATABASE_URL(self):
        return f"postgresql://{self.PG_USER}:{self.PG_PASS}@{self.PG_HOST}/{self.PG_DB}"

    @property
    def REDIS_URL(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"

    model_config = SettingsConfigDict(env_file=".env")
