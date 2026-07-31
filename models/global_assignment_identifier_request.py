from pydantic import BaseModel, Field


class GlobalAssignmentIdentifierRequest(BaseModel):
    dependent_domain: str = Field(alias="dependent-domain", description="""N/A""")
    global_domain: str = Field(alias="global-domain", description="""N/A""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
