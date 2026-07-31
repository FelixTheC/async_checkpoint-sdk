from pydantic import BaseModel, Field


class IdpDefaultAssignmentRequestEdit(BaseModel):
    identity_provider: str = Field(
        alias="identity-provider",
        description="""Represents the Identity Provider to be used for Login by this assignment identified by the name or UID, to cancel existing assignment should set to 'none'.""",
    )
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
