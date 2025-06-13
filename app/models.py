from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class Tag(BaseModel):
    id: str
    name: str


class Author(BaseModel):
    name: str
    image: str


class Metadata(BaseModel):
    confetti: Optional[bool] = None


class Post(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    title: str
    image: str
    content: Optional[str] = None
    description: str
    slug: str
    authorId: str
    teamId: str
    createdAt: datetime
    updatedAt: datetime
    publishedAt: datetime
    metadata: Optional[Metadata] = None
    author: Author
    tags: List[Tag]
