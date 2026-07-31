from pydantic import BaseModel, Field


class StarEncryptedTrafficRequest(BaseModel):
    enabled: bool = Field(
        alias="enabled", description="""Indicates whether to accept all encrypted traffic."""
    )
    community_members: str = Field(
        alias="community-members",
        description="""Indicates on which community members to accept all encrypted traffic.""",
    )
