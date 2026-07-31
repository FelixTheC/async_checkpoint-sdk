from .api_domain_identifier import ApiDomainIdentifier
from .api_object_standard_identifier import ApiObjectStandardIdentifier
from .available_actions_reply import AvailableActionsReply
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .pydantic import BaseModel, Field


class MobileProfileRuleReply(BaseModel):
    name: str = Field(alias="name", description="""Mobile Profile rule name.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    user_groups: list[dict] = Field(
        alias="user-groups",
        description="""User groups that will be configured with the profile - identified by the name or UID.""",
    )
    mobile_profile: ApiObjectStandardIdentifier = Field(
        alias="mobile-profile",
        description="""Profile configuration for User groups - identified by the name or UID.""",
    )
    type: str = Field(alias="type", description="""Object type.""")
    enabled: bool = Field(alias="enabled", description="""Enable/Disable the rule.""")
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
