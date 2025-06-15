from typing import Annotated, List
from fastapi import APIRouter, FastAPI, Query
from app.core.db import db
from app.models import Tag
from app.utils import normalize_mongo_id

router = APIRouter(prefix="/tags", tags=["Tags"])


app = FastAPI()


tags_collection = db.get_collection("tags")


@router.get("/")
async def get_all_tags(
    limit: Annotated[int | None, Query(ge=1, le=1000)] = 20,
) -> List[Tag]:

    tags = []
    data = tags_collection.find({}).limit(limit)
    async for item in data:
        item = normalize_mongo_id(item)
        tags.append(Tag(**item))
    return tags
