from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Acuvault API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
