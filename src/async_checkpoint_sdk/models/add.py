from manual_attachment import ManualAttachment
from pydantic import BaseModel, Field


class Add(BaseModel):
    add: ManualAttachment | list[dict] = Field(
        alias="add", description="""Adds to collection of values"""
    )
