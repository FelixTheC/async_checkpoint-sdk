from pydantic import BaseModel, Field


class BatchRequestDelete(BaseModel):
    objects: list[dict] = Field(
        alias="objects", description="""Batch of objects separated by types."""
    )
