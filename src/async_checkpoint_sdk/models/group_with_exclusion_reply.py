from .api_domain_identifier import ApiDomainIdentifier
from .api_object_standard_identifier import ApiObjectStandardIdentifier
from .available_actions_reply import AvailableActionsReply
from .ip_ranges import IpRanges
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .pydantic import BaseModel, Field


class GroupWithExclusionReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    except_: ApiObjectStandardIdentifier = Field(
        alias="except",
        description="""Name or UID of an object which the group excludes. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    groups: list[dict] = Field(
        alias="groups",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    include: ApiObjectStandardIdentifier = Field(
        alias="include",
        description="""Name or UID of an object which the group includes. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    ranges: IpRanges = Field(
        alias="ranges",
        description="""Displays the group with exclusion's matched content as ranges of IP addresses, in case 'show-as-ranges' is set to true.<br />In this case, the 'include' and 'except' parameters are omitted.""",
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
