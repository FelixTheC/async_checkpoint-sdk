from .pydantic import BaseModel, Field


class UserRequestShow(BaseModel):
    show_certificates: bool = Field(
        alias="show-certificates",
        description="""Indicates whether to calculate and show certificates field in reply.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
