from pydantic import BaseModel, Field


class BatchRequestNew(BaseModel):
    objects: list[dict] = Field(
        alias="objects", description="""Batch of objects separated by types."""
    )
