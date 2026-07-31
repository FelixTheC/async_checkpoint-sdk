from pydantic import BaseModel, Field


class AssignGlobalPolicyRequest(BaseModel):
    dependent_domains: str | list[str] = Field(alias="dependent-domains", description="""N/A""")
    global_domains: str | list[str] = Field(alias="global-domains", description="""N/A""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
