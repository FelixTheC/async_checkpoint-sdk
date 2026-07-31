from .api_domain_identifier import ApiDomainIdentifier
from .available_actions_reply import AvailableActionsReply
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .pydantic import BaseModel, Field


class CompoundGroupReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    description: str = Field(
        alias="description",
        description="""For built-in data types, the description explains the purpose of this type of data representation.
For custom-made data types, you can use this field to provide more details.""",
    )
    matched_groups: list[dict] = Field(
        alias="matched-groups",
        description="""Each one of these data types must be matched - Select existing data types to add. Traffic must match all the data types of this group to match a rule.""",
    )
    unmatched_groups: list[dict] = Field(
        alias="unmatched-groups",
        description="""Each one of these data types must not be matched - Select existing data types to add to the definition. Traffic that does not contain any data matching the types in this list will match this compound data type.""",
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
