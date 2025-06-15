from fastapi import APIRouter
from app.routes import posts, categories, tags


api_router = APIRouter()
api_router.include_router(posts.router)
api_router.include_router(categories.router)
api_router.include_router(tags.router)
