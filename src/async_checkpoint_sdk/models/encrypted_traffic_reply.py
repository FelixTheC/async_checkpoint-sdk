from pydantic import BaseModel, Field


class EncryptedTrafficReply(BaseModel):
    enabled: bool = Field(
        alias="enabled", description="""Indicates whether to accept all encrypted traffic."""
    )
