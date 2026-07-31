from pydantic import BaseModel, Field


class NatSectionIdentifierRequest(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    package: str = Field(alias="package", description="""Name of the package.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
