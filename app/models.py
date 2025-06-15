from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class Tag(BaseModel):
    id: str
    name: str
    slug: str


class Category(BaseModel):
    id: str
    name: str
    description: str | None = None
    slug: str
    date: datetime | None = None


class Author(BaseModel):
    name: str
    image: str


class Metadata(BaseModel):
    confetti: bool | None = None


class Post(BaseModel):
    id: str | None = Field(None, alias="_id")
    title: str
    image: str
    content: str | None = None
    description: str
    slug: str
    authorId: str
    teamId: str
    createdAt: datetime
    updatedAt: datetime
    publishedAt: datetime
    metadata: Metadata | None = None
    author: Author
    tags: List[Tag]
    category: Category
