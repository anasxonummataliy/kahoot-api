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
    ACCESS_TOKEN_EXPIRE_MINUTES:int

    @property
    def async_db_url(self):
        return f"postgresql+asyncpg://{self.PG_USER}:{self.PG_PASS}@{self.PG_HOST}/{self.PG_DB}"

    @property
    def db_url(self):
        return f"postgresql://{self.PG_USER}:{self.PG_PASS}@{self.PG_HOST}/{self.PG_DB}"

    model_config = SettingsConfigDict(env_file=".env")
