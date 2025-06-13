from typing import List
from fastapi import APIRouter, Body, FastAPI, HTTPException

from app.core.db import db
from app.models import Post
from app.utils import normalize_mongo_id


router = APIRouter(prefix="/posts", tags=["Posts"])


app = FastAPI()

posts_collection = db.get_collection("posts")


@router.get("/")
async def get_posts(limit: int = 10) -> List[Post]:
    posts = []
    data = posts_collection.find({}).limit(limit)
    async for item in data:
        item = normalize_mongo_id(item)
        posts.append(Post(**item))
    return posts


@router.get("/{slug}")
async def get_post_by_slug(
    slug: str = "viagem-sustentavel-reduzindo-seu-impacto-na-estrada",
) -> Post:
    data = await posts_collection.find_one({"slug": slug})
    if not data:
        raise HTTPException(status_code=404, detail="Post not found")
    data = normalize_mongo_id(data)
    return data
