from pydantic import BaseModel, Field


class ShowHaStatusReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    domain_type: str = Field(alias="domain-type", description="""Domain type.""")
    servers: list[dict] = Field(alias="servers", description="""Servers state.""")
    successfully_synced: bool = Field(
        alias="successfully-synced", description="""The HA status of the domain."""
    )
