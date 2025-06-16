from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mongodb_url: str
    version: str
    app_name: str
    app_summary: str
    api_v1: str
    api_key: str


settings = Settings()

app = FastAPI()


@app.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
    }
