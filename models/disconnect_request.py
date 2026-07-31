from pydantic import BaseModel, Field


class DisconnectRequest(BaseModel):
    discard: bool = Field(
        alias="discard",
        description="""Discard all changes committed during the session.""",
    )
