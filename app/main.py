from fastapi import FastAPI
from fastapi.security import HTTPBearer
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.exceptions import (
    http_exception_handler,
    validation_exception_handler,
    generic_exception_handler,
)


from app.core.config import settings
from app.routes.main import api_router

from app.core.security import APIKeyMiddleware
from app.utils import custom_openapi

bearer_scheme = HTTPBearer()

app = FastAPI(
    title=settings.app_name,
    summary=settings.app_summary,
)

app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

app.openapi = lambda: custom_openapi(
    app,
    title=settings.app_name,
    version=settings.version,
    description=settings.app_summary,
)


origins = [
    "http://localhost:3000",
    "http://localhost",
    "http://datapanp.com",
    "http://www.datapanp.com",
    "https://datapanp.com",
    "https://www.datapanp.com",
]


@app.middleware("http")
async def securityMiddleware(request, call_next):
    return await APIKeyMiddleware(request, call_next)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_router, prefix=settings.api_v1)
