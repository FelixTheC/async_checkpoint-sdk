from api_domain_identifier import ApiDomainIdentifier
from api_object_standard_identifier import ApiObjectStandardIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class LdapGroupReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    account_unit: ApiObjectStandardIdentifier = Field(
        alias="account-unit",
        description="""LDAP account unit of the group. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    scope: str = Field(
        alias="scope",
        description="""Group's scope. There are three possible ways of defining a group, based on the users defined on the Account Unit.""",
    )
    account_unit_branch: str = Field(
        alias="account-unit-branch", description="""Branch of the selected LDAP Account Unit."""
    )
    sub_tree_prefix: str = Field(
        alias="sub-tree-prefix", description="""Sub tree prefix of the selected branch."""
    )
    group_prefix: str = Field(
        alias="group-prefix", description="""Group name in the selected branch."""
    )
    apply_filter_for_dynamic_group: bool = Field(
        alias="apply-filter-for-dynamic-group",
        description="""Indicate whether to apply LDAP filter for dynamic group.""",
    )
    ldap_filter: str = Field(
        alias="ldap-filter", description="""LDAP filter for the dynamic group."""
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain", description="""Information about the domain that holds the Object."""
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
        alias="available-actions", description="""Actions that are available on the object."""
    )
