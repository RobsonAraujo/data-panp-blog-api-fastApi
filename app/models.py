from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class TagBase(BaseModel):
    name: str
    slug: str
    description: str | None = None


class Tag(TagBase):
    id: str | None = Field(None, alias="_id")


class TagInPost(TagBase):
    id: str


class CategoryBase(BaseModel):
    name: str
    description: str | None = None
    slug: str
    created_at: datetime | None = None


class Category(CategoryBase):
    id: str | None = Field(None, alias="_id")


class CategoryInPost(CategoryBase):
    id: str


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
    tags: List[TagInPost]
    category: CategoryInPost
