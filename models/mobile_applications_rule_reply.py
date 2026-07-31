from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class MobileApplicationsRuleReply(BaseModel):
    name: str = Field(alias="name", description="""Mobile Access rule name.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    user_groups: list[dict] = Field(
        alias="user-groups",
        description="""User groups that will be associated with the apps - identified by the name or UID.""",
    )
    applications: list[dict] = Field(
        alias="applications",
        description="""Available apps that will be associated with the user groups - identified by the name or UID.""",
    )
    type: str = Field(alias="type", description="""Object type.""")
    enabled: bool = Field(alias="enabled", description="""Enable/Disable the rule.""")
    install_on: list[dict] = Field(
        alias="install-on",
        description="""Which gateway, identified by the name or UID, to install the policy. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
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
