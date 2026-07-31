from .add import add
from .api_doc_rule_base_position_object_builder import (
    ApiDocRuleBasePositionObjectBuilder,
)
from .pydantic import BaseModel, Field
from .remove import remove


class MobileApplicationsRuleRequestEdit(BaseModel):
    user_groups: add | remove | str | list[str] = Field(
        alias="user-groups",
        description="""User groups that will be associated with the apps - identified by the name or UID.""",
    )
    applications: add | remove | str | list[str] = Field(
        alias="applications",
        description="""Available apps that will be associated with the user groups - identified by the name or UID.""",
    )
    enabled: bool = Field(alias="enabled", description="""Enable/Disable the rule.""")
    install_on: add | remove | str | list[str] = Field(
        alias="install-on",
        description="""Which Gateways identified by the name or UID to install the policy on.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    new_position: int | str | ApiDocRuleBasePositionObjectBuilder = Field(
        alias="new-position", description="""New position in the rulebase."""
    )
    tags: add | remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
