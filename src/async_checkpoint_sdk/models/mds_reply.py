from api_domain_identifier import ApiDomainIdentifier
from api_object_standard_identifier import ApiObjectStandardIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class MdsReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    domains: list[dict] = Field(
        alias="domains",
        description="""Collection of Domain objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    global_domains: list[dict] = Field(
        alias="global-domains",
        description="""Collection of Global domain objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    hardware: ApiObjectStandardIdentifier = Field(
        alias="hardware",
        description="""Hardware. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    ip_pool_first: str = Field(
        alias="ip-pool-first", description="""Start of IP address pool range."""
    )
    ip_pool_last: str = Field(alias="ip-pool-last", description="""End of IP address pool range.""")
    ipv4_address: str = Field(alias="ipv4-address", description="""IPv4 address.""")
    ipv6_address: str = Field(alias="ipv6-address", description="""IPv6 address.""")
    os: ApiObjectStandardIdentifier = Field(
        alias="os",
        description="""Operating System. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    platform: ApiObjectStandardIdentifier = Field(
        alias="platform",
        description="""Platform. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    server_type: str = Field(alias="server-type", description="""Type of the management server.""")
    sic_name: str = Field(
        alias="sic-name", description="""Name of the Secure Internal Connection Trust."""
    )
    sic_state: str = Field(
        alias="sic-state", description="""State the Secure Internal Connection Trust."""
    )
    version: ApiObjectStandardIdentifier = Field(
        alias="version",
        description="""System Version. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
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
