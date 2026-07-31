from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class TrustedClientReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    domains_assignment: list[dict] = Field(
        alias="domains-assignment",
        description="""Domains assignment. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    ipv4_address: str = Field(alias="ipv4-address", description="""IPv4 address.""")
    ipv4_address_first: str = Field(
        alias="ipv4-address-first", description="""First IPv4 address in the range."""
    )
    ipv4_address_last: str = Field(
        alias="ipv4-address-last", description="""Last IPv4 address in the range."""
    )
    ipv6_address: str = Field(alias="ipv6-address", description="""IPv6 address.""")
    ipv6_address_first: str = Field(
        alias="ipv6-address-first", description="""First IPv6 address in the range."""
    )
    ipv6_address_last: str = Field(
        alias="ipv6-address-last", description="""Last IPv6 address in the range."""
    )
    mask_length4: int = Field(alias="mask-length4", description="""IPv4 mask length.""")
    mask_length6: int = Field(alias="mask-length6", description="""IPv6 mask length.""")
    multi_domain_server_trusted_client: bool = Field(
        alias="multi-domain-server-trusted-client",
        description="""Let this trusted client connect to all Multi-Domain Servers in the deployment.""",
    )
    subnet_mask4: str = Field(alias="subnet-mask4", description="""IPv4 mask.""")
    type: str = Field(alias="type", description="""Trusted client type.""")
    wild_card: str = Field(alias="wild-card", description="""IP wild card (e.g. 192.0.2.*).""")
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain", description="""Information about the domain that holds the Object."""
    )
    icon: str = Field(alias="icon", description="""Object icon.""")
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
    read_only: bool = Field(
        alias="read-only", description="""Indicates whether the object is read-only."""
    )
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions", description="""Actions that are available on the object."""
    )
