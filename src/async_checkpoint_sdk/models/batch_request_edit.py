from pydantic import BaseModel, Field


class BatchRequestEdit(BaseModel):
    objects: list[dict] = Field(
        alias="objects", description="""Batch of objects separated by types."""
    )
