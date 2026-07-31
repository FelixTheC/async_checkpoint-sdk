from pydantic import BaseModel, Field
from trust_details_reply import TrustDetailsReply


class ClusterMemberReply(BaseModel):
    name: str = Field(alias="name", description="""N/A""")
    uid: str = Field(alias="uid", description="""Cluster member object UID.""")
    auto_generate_ip: bool = Field(
        alias="auto-generate-ip",
        description="""Use an automatically generated IP address for the Gateway object (applies only to Smart-1 Cloud).""",
    )
    interfaces: list[dict] = Field(
        alias="interfaces", description="""Cluster member network interfaces."""
    )
    ip_address: str = Field(alias="ip-address", description="""Cluster member IP address.""")
    ipv6_address: str = Field(alias="ipv6-address", description="""Cluster member IPv6 address.""")
    sic_message: str = Field(
        alias="sic-message", description="""Secure Internal Communication message."""
    )
    sic_state: str = Field(
        alias="sic-state", description="""Secure Internal Communication state."""
    )
    trust_details: TrustDetailsReply = Field(
        alias="trust-details", description="""Details for trusted communication."""
    )
    trust_method: str = Field(
        alias="trust-method",
        description="""Trust method that was used for establishing communication.""",
    )
    priority: int = Field(
        alias="priority",
        description="""In a High Availability New mode cluster each machine is given a priority. The highest priority machine serves as the gateway in normal circumstances. If this machine fails, control is passed to the next highest priority machine. If that machine fails, control is passed to the next machine, and so on.
In Load Sharing Unicast mode cluster, the highest priority is the pivot machine.
The values must be in a range from 1 to N, where N is number of cluster members.""",
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
