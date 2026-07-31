from .pydantic import BaseModel, Field


class VpnDomainRequest(BaseModel):
    limit_peer_domain_size: bool = Field(
        alias="limit-peer-domain-size",
        description="""Use this parameter to limit the number of IP addresses in the VPN Domain of each peer according to the value in the max-allowed-addresses field.""",
    )
    max_allowed_addresses: int = Field(
        alias="max-allowed-addresses",
        description="""Maximum number of IP addresses in the VPN Domain of each peer. This value will be enforced only when limit-peer-domain-size field is set to true. Select a value between 1 and 256. Default value is 256.""",
    )
