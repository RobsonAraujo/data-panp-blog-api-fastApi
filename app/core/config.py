from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Data PANP - Blog"
    app_summary: str = "Data PANP - Rest API"
    mongodb_url: str = ""
    api_v1: str = ""
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
app = FastAPI()


@app.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
    }
