from typing import Optional

from pydantic import BaseModel, ConfigDict, HttpUrl, Field


class LinkModel(BaseModel):
    original_url: Optional[str] = Field(None, description="Original URL")
    short_url: Optional[str] = Field(None, description="Short URL")
    slug: Optional[str] = Field(None, min_length=6, max_length=6, description="Slug")

    model_config = ConfigDict(from_attributes=True)
