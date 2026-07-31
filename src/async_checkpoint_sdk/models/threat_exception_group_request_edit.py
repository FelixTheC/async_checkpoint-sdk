from add import Add
from pydantic import BaseModel, Field
from remove import Remove


class ThreatExceptionGroupRequestEdit(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    applied_profile: str = Field(
        alias="applied-profile",
        description="""The threat profile to apply this group to in the case of apply-on threat-rules-with-specific-profile.""",
    )
    applied_threat_rules: Add | Remove = Field(
        alias="applied-threat-rules",
        description="""The threat rules to apply this group on in the case of apply-on manually-select-threat-rules.""",
    )
    apply_on: str = Field(
        alias="apply-on",
        description="""An exception group can be set to apply on all threat rules, all threat rules which have a specific profile, or those rules manually chosen by the user.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    tags: Add | Remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
