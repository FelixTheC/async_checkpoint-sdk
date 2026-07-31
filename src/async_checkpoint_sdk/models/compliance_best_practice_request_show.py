from .pydantic import BaseModel, Field


class ComplianceBestPracticeRequestShow(BaseModel):
    show_regulations: bool = Field(
        alias="show-regulations",
        description="""Show the applicable regulations of the Best Practice.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
