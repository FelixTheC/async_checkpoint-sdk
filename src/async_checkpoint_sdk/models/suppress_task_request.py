from .pydantic import BaseModel, Field


class SuppressTaskRequest(BaseModel):
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Ignore warnings if exist."""
    )
