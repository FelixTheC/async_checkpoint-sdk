from .api_domain_identifier import ApiDomainIdentifier
from .available_actions_reply import AvailableActionsReply
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .nat_settings_reply import NatSettingsReply
from .pydantic import BaseModel, Field
from .vsx_blades_reply import VsxBladesReply


class VsxClusterReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    hit_count: bool = Field(alias="hit-count", description="""Status of rule hit count for FW1.""")
    interfaces: list[dict] = Field(alias="interfaces", description="""Network interfaces.""")
    ipv4_address: str = Field(alias="ipv4-address", description="""N/A""")
    ipv6_address: str = Field(alias="ipv6-address", description="""N/A""")
    nat_settings: NatSettingsReply = Field(alias="nat-settings", description="""NAT settings.""")
    network_security_blades: VsxBladesReply = Field(
        alias="network-security-blades", description="""Network Security Blades."""
    )
    version: str = Field(alias="version", description="""N/A""")
    virtual_systems: list[dict] = Field(
        alias="virtual-systems",
        description="""Virtual Systems belonging to this VSX Cluster.""",
    )
    policy: list[dict] = Field(alias="policy", description="""Installed policy packages.""")
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
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
