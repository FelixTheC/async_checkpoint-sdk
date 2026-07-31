from add import Add
from api_doc_rule_base_position_object_builder import ApiDocRuleBasePositionObjectBuilder
from pydantic import BaseModel, Field
from remove import Remove


class MobileProfileRuleRequestEdit(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    mobile_profile: str = Field(
        alias="mobile-profile",
        description="""Profile configuration for User groups - identified by the name or UID.""",
    )
    user_groups: Add | Remove | str | list[str] = Field(
        alias="user-groups",
        description="""User groups that will be configured with the profile object - identified by the name or UID.""",
    )
    enabled: bool = Field(alias="enabled", description="""Enable/Disable the rule.""")
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    new_position: int | str | ApiDocRuleBasePositionObjectBuilder = Field(
        alias="new-position", description="""New position in the rulebase."""
    )
    tags: Add | Remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
