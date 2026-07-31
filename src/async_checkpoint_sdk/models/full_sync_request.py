from .pydantic import BaseModel, Field


class FullSyncRequest(BaseModel):
    ignore_errors: bool = Field(
        alias="ignore-errors", description="""Apply changes ignoring errors."""
    )
