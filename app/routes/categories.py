from typing import Annotated, List
from fastapi import APIRouter, FastAPI, Query
from app.core.db import db
from app.utils import normalize_mongo_id
from app.models import Category

router = APIRouter(prefix="/categories", tags=["Categories"])


app = FastAPI()


categories_collection = db.get_collection("categories")


@router.get("/")
async def get_all_categories(
    limit: Annotated[int | None, Query(ge=1, le=1000)] = 20,
) -> List[Category]:

    categories = []
    data = categories_collection.find({}).limit(limit)
    async for item in data:
        item = normalize_mongo_id(item)
        categories.append(Category(**item))
    return categories
