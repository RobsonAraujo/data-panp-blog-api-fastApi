from fastapi import APIRouter, FastAPI
from app.core.db import db

router = APIRouter(prefix="/posts", tags=["Posts"])


app = FastAPI()

posts_collection = db.get_collection("posts")


@router.get("/")
async def get_posts():
    posts = []
    cursor = posts_collection.find({})
    async for document in cursor:
        document["_id"] = str(document["_id"])
        posts.append(document)
    return {"data": posts}
