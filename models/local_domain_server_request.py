from pydantic import BaseModel, Field


class LocalDomainServerRequest(BaseModel):
    active: bool = Field(
        alias="active",
        description="""Activate domain server. Only one domain server is allowed to be active.""",
    )
    ipv6_address: str = Field(
        alias="ipv6-address", description="""IPv6 address. Can only be set one time."""
    )
    skip_start_domain_server: bool = Field(
        alias="skip-start-domain-server",
        description="""Set this value to be true to prevent starting the new created domain.""",
    )
    type: str = Field(alias="type", description="""Domain server type.""")
