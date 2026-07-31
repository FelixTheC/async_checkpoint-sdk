from .api_domain_identifier import ApiDomainIdentifier
from .pydantic import BaseModel, Field


class InterfaceStandardReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    cluster_members: list[dict] = Field(
        alias="cluster-members", description="""Cluster members uid and IP address."""
    )
    cluster_network_type: str = Field(
        alias="cluster-network-type", description="""Cluster interface type."""
    )
    comments: str = Field(alias="comments", description="""N/A""")
    ip_addresses: str = Field(
        alias="ip-addresses",
        description="""IPv4 and IPv6 network address and network mask length or cluster network type.""",
    )
    topology: str = Field(alias="topology", description="""Topology configuration.""")
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    icon: str = Field(alias="icon", description="""Object icon.""")
