from .pydantic import BaseModel, Field


class BaseDomainServerReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    active: bool = Field(alias="active", description="""Domain server status.""")
    ipv4_address: str = Field(alias="ipv4-address", description="""IPv4 address.""")
    ipv6_address: str = Field(alias="ipv6-address", description="""IPv6 address.""")
    multi_domain_server: str = Field(
        alias="multi-domain-server", description="""Multi Domain server name or UID."""
    )
    skip_start_domain_server: bool = Field(
        alias="skip-start-domain-server",
        description="""Set this value to be true to prevent starting the new created domain.""",
    )
    type: str = Field(alias="type", description="""Domain server type.""")
