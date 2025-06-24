import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "MyFastAPI"
    database_url: str

    class Config:
        env_file = ".env"
        # Environment variables have priority over .env file
        case_sensitive = False

# For Render deployment, prefer environment variables
settings = Settings()
