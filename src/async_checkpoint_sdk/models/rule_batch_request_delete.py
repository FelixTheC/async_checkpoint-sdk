from pydantic import BaseModel, Field


class RuleBatchRequestDelete(BaseModel):
    objects: list[dict] = Field(
        alias="objects", description="""Batch of rules separated by types."""
    )
