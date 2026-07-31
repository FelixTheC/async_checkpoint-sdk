from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class InfinityIdpObjectReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    description: str = Field(alias="description", description="""Description string.""")
    display_name: str = Field(
        alias="display-name", description="""Entity name in the Management Server."""
    )
    ext_id: str = Field(
        alias="ext-id",
        description="""Entity unique identifier in the Identity Provider.""",
    )
    idp_display_name: str = Field(
        alias="idp-display-name",
        description="""Identity Provider name in Management Server.""",
    )
    idp_id: str = Field(
        alias="idp-id",
        description="""Identity Provider unique identifier in Infinity Portal.""",
    )
    idp_name: str = Field(
        alias="idp-name", description="""Identity Provider name in Infinity Portal."""
    )
    object_type: str = Field(
        alias="object-type", description="""Entity type - can be user/group/machine."""
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
