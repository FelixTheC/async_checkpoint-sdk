from pydantic import BaseModel, Field


class LocalDomainServerRequestUpdate(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    multi_domain_server: str = Field(
        alias="multi-domain-server", description="""Multi Domain server name or UID."""
    )
    ipv6_address: str = Field(
        alias="ipv6-address", description="""IPv6 address. Can only be set one time."""
    )
    restart_domain_server: bool = Field(
        alias="restart-domain-server",
        description="""Set to true for restarting the domain server after updating Ipv6 Address.""",
    )
