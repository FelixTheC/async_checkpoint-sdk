from pydantic import BaseModel, Field


class LoginMessageRequestSet(BaseModel):
    header: str = Field(alias="header", description="""Login message header.""")
    message: str = Field(alias="message", description="""Login message body.""")
    show_message: bool = Field(
        alias="show-message", description="""Whether to show login message."""
    )
    warning: bool = Field(alias="warning", description="""Add warning sign.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
