from pydantic import BaseModel, Field


class SecurityAccessDefaultsReply(BaseModel):
    destination: str = Field(
        alias="destination", description="""Destination default value identified by name."""
    )
    service: str = Field(
        alias="service",
        description="""Service and Applications default value identified by name.""",
    )
    source: str = Field(alias="source", description="""Source default value identified by name.""")
    track: str = Field(alias="track", description="""Track default value identified by name.""")
