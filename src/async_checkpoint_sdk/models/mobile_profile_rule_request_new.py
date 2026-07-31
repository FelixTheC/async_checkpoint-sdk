from api_doc_rule_base_position_object_builder import ApiDocRuleBasePositionObjectBuilder
from pydantic import BaseModel, Field


class MobileProfileRuleRequestNew(BaseModel):
    position: int | str | ApiDocRuleBasePositionObjectBuilder = Field(
        alias="position", description="""Position in the rulebase."""
    )
    name: str = Field(alias="name", description="""Mobile Profile rule name.""")
    mobile_profile: str = Field(
        alias="mobile-profile",
        description="""Profile configuration for User groups - identified by the name or UID.""",
    )
    user_groups: str | list[str] = Field(
        alias="user-groups",
        description="""User groups that will be configured with the profile object - identified by the name or UID.""",
    )
    enabled: bool = Field(alias="enabled", description="""Enable/Disable the rule.""")
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
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
