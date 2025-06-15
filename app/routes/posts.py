from typing import List, Annotated
from fastapi import APIRouter, Query, Path, Body, FastAPI, HTTPException

from app.core.db import db
from app.models import Post
from app.utils import normalize_mongo_id
from app.data_doc import postReturn
from bson import ObjectId


router = APIRouter(prefix="/posts", tags=["Posts"])


app = FastAPI()

posts_collection = db.get_collection("posts")


@router.get("/")
async def get_post(
    limit: Annotated[int | None, Query(ge=1, le=1000)] = 6,
    offset: Annotated[int, Query(ge=0)] = 0,
    categoryId: Annotated[str | None, Query(max_length=150)] = None,
    categorySlug: Annotated[str | None, Query(max_length=100)] = None,
    tagId: Annotated[str | None, Query(max_length=150)] = None,
    tagSlug: Annotated[str | None, Query(max_length=100)] = None,
    search: Annotated[str | None, Query(max_length=300)] = None,
) -> List[Post]:
    posts = []

    query = {}

    if categoryId:
        query["category.id"] = categoryId

    if categorySlug:
        query["category.slug"] = {"$regex": categorySlug, "$options": "i"}

    if tagSlug:
        query["tags.slug"] = {"$regex": tagSlug, "$options": "i"}

    if tagId:
        query["tags.id"] = tagId

    if search:
        query["$or"] = [
            {"title": {"$regex": search, "$options": "i"}},
            {"description": {"$regex": search, "$options": "i"}},
            {"content": {"$regex": search, "$options": "i"}},
        ]

    data = posts_collection.find(query).skip(offset).limit(limit)
    async for item in data:
        item = normalize_mongo_id(item)
        posts.append(Post(**item))
    return posts


@router.get("/{slug}")
async def get_by_slug(
    slug: Annotated[str, Path(max_length=200)],
) -> Post:
    data = await posts_collection.find_one({"slug": slug})
    if not data:
        raise HTTPException(status_code=404, detail="Post not found")
    data = normalize_mongo_id(data)
    return data


@router.get("/related/{post_id}")
async def get_related_posts(
    post_id: Annotated[str, Path(max_length=200)],
    limit: Annotated[int, Query(ge=1, le=1000)] = 4,
) -> List[Post]:

    post = await posts_collection.find_one({"_id": ObjectId(post_id)})
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    category_id = post.get("category", {}).get("id")
    tags = post.get("tags", [])
    tag_ids = [tag["id"] for tag in tags]

    query = {
        "_id": {"$ne": ObjectId(post_id)},
        "$or": [{"category.id": category_id}, {"tags.id": {"$in": tag_ids}}],
    }

    related_posts = []
    result = posts_collection.find(query).limit(limit)
    async for item in result:
        item = normalize_mongo_id(item)
        related_posts.append(Post(**item))

    return related_posts


@router.post("/create")
async def create(
    post: Annotated[
        Post,
        Body(examples=[postReturn]),
    ],
) -> Post:
    post_dict = post.model_dump(by_alias=True)

    if post_dict.get("_id") is None:
        post_dict.pop("_id")

    result = await posts_collection.insert_one(post_dict)
    created_post = await posts_collection.find_one({"_id": result.inserted_id})
    if not created_post:
        raise HTTPException(status_code=500, detail="Post not created")
    created_post = normalize_mongo_id(created_post)
    return created_post
