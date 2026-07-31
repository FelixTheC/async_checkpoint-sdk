from .api_date_reply import ApiDateReply
from .pydantic import BaseModel, Field


class HaStatusPeerReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    ip_address: str = Field(alias="ip-address", description="""Server IPv4 or IPv6 address.""")
    ha_state: str = Field(alias="ha-state", description="""High availability state.""")
    last_successful_sync: ApiDateReply = Field(
        alias="last-successful-sync", description="""Last Successful Sync Time."""
    )
    sync_state: str = Field(
        alias="sync-state", description="""Sync State - shown only for standby peers."""
    )
    multi_domain_server: str = Field(
        alias="multi-domain-server", description="""Multi Domain server name."""
    )
