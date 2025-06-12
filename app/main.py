from fastapi import FastAPI


from app.core.config import settings
from app.routes.main import api_router


app = FastAPI(
    title=settings.app_name,
    summary=settings.app_summary,
)

app.include_router(api_router, prefix=settings.api_v1)
