from .pydantic import BaseModel, Field


class HaStatePeerReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    ip_address: str = Field(alias="ip-address", description="""Server IPv4 or IPv6 address.""")
    ha_state: str = Field(alias="ha-state", description="""High availability state.""")
    multi_domain_server: str = Field(
        alias="multi-domain-server", description="""Multi Domain server name."""
    )
