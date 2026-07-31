from pydantic import BaseModel, Field


class DisconnectRequest(BaseModel):
    uid: str = Field(alias="uid", description="""Session unique identifier.""")
    discard: bool = Field(
        alias="discard", description="""Discard all changes committed during the session."""
    )
