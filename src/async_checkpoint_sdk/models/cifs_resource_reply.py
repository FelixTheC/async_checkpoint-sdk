from .api_domain_identifier import ApiDomainIdentifier
from .available_actions_reply import AvailableActionsReply
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .pydantic import BaseModel, Field


class CifsResourceReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    allowed_disk_and_print_shares: list[dict] = Field(
        alias="allowed-disk-and-print-shares",
        description="""The list of Allowed Disk and Print Shares. Must be added in pairs.""",
    )
    type: str = Field(alias="type", description="""Object type.""")
    log_mapped_shares: bool = Field(
        alias="log-mapped-shares", description="""Logs each share map attempt."""
    )
    log_access_violation: bool = Field(
        alias="log-access-violation",
        description="""Logs any attempt to violate the restrictions imposed by the Resource.""",
    )
    block_remote_registry_access: bool = Field(
        alias="block-remote-registry-access",
        description="""Blocks the ability to remotely manipulate a the window's registry.""",
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
