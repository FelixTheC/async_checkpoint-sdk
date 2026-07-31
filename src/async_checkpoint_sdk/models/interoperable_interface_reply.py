from .api_domain_identifier import ApiDomainIdentifier
from .available_actions_reply import AvailableActionsReply
from .internal_topology_settings_reply import InternalTopologySettingsReply
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .pydantic import BaseModel, Field


class InteroperableInterfaceReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    ipv4_address: str = Field(alias="ipv4-address", description="""IPv4 address.""")
    ipv4_mask_length: int = Field(
        alias="ipv4-mask-length", description="""IPv4 network mask length."""
    )
    ipv4_network_mask: str = Field(alias="ipv4-network-mask", description="""IPv4 network mask.""")
    ipv6_address: str = Field(alias="ipv6-address", description="""IPv6 address.""")
    ipv6_mask_length: int = Field(
        alias="ipv6-mask-length", description="""IPv6 network mask length."""
    )
    ipv6_network_mask: str = Field(alias="ipv6-network-mask", description="""IPv6 network mask.""")
    topology: str = Field(alias="topology", description="""Topology configuration.""")
    topology_settings: InternalTopologySettingsReply = Field(
        alias="topology-settings", description="""Internal topology settings."""
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    icon: str = Field(alias="icon", description="""Object icon.""")
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
    read_only: bool = Field(
        alias="read-only", description="""Indicates whether the object is read-only."""
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
