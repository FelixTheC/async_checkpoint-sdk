from .pydantic import BaseModel, Field


class ShowLogsRequest(BaseModel):
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Ignore warnings if exist."""
    )
