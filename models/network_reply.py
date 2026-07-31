from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from nat_settings_reply import NatSettingsReply
from pydantic import BaseModel, Field


class NetworkReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    subnet4: str = Field(alias="subnet4", description="""IPv4 network address.""")
    subnet6: str = Field(alias="subnet6", description="""IPv6 network address.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    broadcast: str = Field(
        alias="broadcast", description="""Allow broadcast address inclusion."""
    )
    mask_length4: int = Field(
        alias="mask-length4", description="""IPv4 network mask length."""
    )
    mask_length6: int = Field(
        alias="mask-length6", description="""IPv6 network mask length."""
    )
    subnet_mask: str = Field(alias="subnet-mask", description="""IPv4 network mask.""")
    type: str = Field(alias="type", description="""Object type.""")
    groups: list[dict] = Field(
        alias="groups",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    nat_settings: NatSettingsReply = Field(
        alias="nat-settings", description="""NAT settings."""
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
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
