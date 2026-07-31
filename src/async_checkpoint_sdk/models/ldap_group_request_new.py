from .pydantic import BaseModel, Field


class LdapGroupRequestNew(BaseModel):
    scope: str = Field(
        alias="scope",
        description="""Group's scope. There are three possible ways of defining a group, based on the users defined on the Account Unit.""",
    )
    account_unit_branch: str = Field(
        alias="account-unit-branch",
        description="""Branch of the selected LDAP Account Unit.""",
    )
    sub_tree_prefix: str = Field(
        alias="sub-tree-prefix",
        description="""Sub tree prefix of the selected branch. <font color=red>Relevant only when</font> 'scope' is set to 'only_sub_prefix'. Must be in DN syntax.""",
    )
    group_prefix: str = Field(
        alias="group-prefix",
        description="""Group name in the selected branch. <font color=red>Required only when</font> 'scope' is set to 'only_group_in_branch'. Must be in DN syntax.""",
    )
    apply_filter_for_dynamic_group: bool = Field(
        alias="apply-filter-for-dynamic-group",
        description="""Indicate whether to apply LDAP filter for dynamic group. <font color=red>Relevant only when</font> 'scope' is not set to 'only_group_in_branch'.""",
    )
    ldap_filter: str = Field(
        alias="ldap-filter",
        description="""LDAP filter for the dynamic group. <font color=red>Relevant only when</font> 'apply-filter-for-dynamic-group' is set to 'true'.""",
    )
    set_if_exists: bool = Field(
        alias="set-if-exists",
        description="""If another object with the same identifier already exists, it will be updated. The command behaviour will be the same as if originally a set command was called. Pay attention that original object's fields will be overwritten by the fields provided in the request payload!""",
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from .the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
    )
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
