from .pydantic import BaseModel, Field


class DynamicObjectReply(BaseModel):
    comments: str = Field(alias="comments", description="""Comments.""")
    name: str = Field(alias="name", description="""Name.""")
    resolved_ip_addresses: list[dict] = Field(
        alias="resolved-ip-addresses", description="""Resolved IP Addresses."""
    )
    uid: str = Field(alias="uid", description="""UID.""")
