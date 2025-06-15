from fastapi import FastAPI, HTTPException, Request
from app.core.config import settings

app = FastAPI()


async def APIKeyMiddleware(request: Request, call_next):
    if request.url.path.startswith("/docs") or request.url.path.startswith(
        "/openapi.json"
    ):
        return await call_next(request)

    auth_header = request.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(status_code=422, detail="Missing Authorization Header")
    token = auth_header.split("Bearer ")[1]
    if token != settings.api_key:
        raise HTTPException(status_code=403, detail="Unauthorized")

    response = await call_next(request)
    return response
