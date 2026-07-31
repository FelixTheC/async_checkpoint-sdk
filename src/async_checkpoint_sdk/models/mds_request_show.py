from .pydantic import BaseModel, Field


class MdsRequestShow(BaseModel):
    show_domains: bool = Field(
        alias="show-domains",
        description="""Indicates whether to show domains field in reply.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
