from pydantic import BaseModel, Field


class ComplianceGaiaBestPracticeRequestShow(BaseModel):
    best_practice_id: str = Field(alias="best-practice-id", description="""Best Practice ID.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
