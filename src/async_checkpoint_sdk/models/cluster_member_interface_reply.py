from pydantic import BaseModel, Field


class ClusterMemberInterfaceReply(BaseModel):
    ipv4_address: str = Field(alias="ipv4-address", description="""IPv4 address.""")
    ipv4_mask_length: int = Field(
        alias="ipv4-mask-length", description="""IPv4 network mask length."""
    )
    ipv4_network_mask: str = Field(alias="ipv4-network-mask", description="""IPv4 network mask.""")
    name: str = Field(alias="name", description="""Cluster member interface name.""")
    ipv6_address: str = Field(alias="ipv6-address", description="""IPv6 address.""")
    ipv6_mask_length: int = Field(
        alias="ipv6-mask-length", description="""IPv6 network mask length."""
    )
    ipv6_network_mask: str = Field(alias="ipv6-network-mask", description="""IPv6 network mask.""")
    uid: str = Field(alias="uid", description="""Cluster member interface object UID.""")
