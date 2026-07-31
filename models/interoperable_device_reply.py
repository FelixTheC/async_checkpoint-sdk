from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field
from vpn_settings_reply import VpnSettingsReply


class InteroperableDeviceReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    ipv4_address: str = Field(
        alias="ipv4-address",
        description="""IPv4 address of the Interoperable Device.""",
    )
    ipv6_address: str = Field(
        alias="ipv6-address",
        description="""IPv6 address of the Interoperable Device.""",
    )
    autonomous_system_number: str = Field(
        alias="autonomous-system-number",
        description="""The Autonomous System Number (ASN) for this Interoperable Device object.""",
    )
    interfaces: list[dict] = Field(
        alias="interfaces", description="""Interoperable Device interfaces."""
    )
    vpn_settings: VpnSettingsReply = Field(
        alias="vpn-settings",
        description="""VPN domain properties for the Interoperable Device.""",
    )
    groups: list[dict] = Field(
        alias="groups",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    type: str = Field(alias="type", description="""Object type.""")
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
