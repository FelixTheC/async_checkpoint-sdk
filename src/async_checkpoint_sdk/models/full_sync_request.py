from pydantic import BaseModel, Field


class FullSyncRequest(BaseModel):
    name: str = Field(
        alias="name",
        description="""Peer name (Multi Domain Server, Domain Server or Security Management Server).""",
    )
    ignore_errors: bool = Field(
        alias="ignore-errors", description="""Apply changes ignoring errors."""
    )
