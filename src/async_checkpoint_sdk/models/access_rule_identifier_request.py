from pydantic import BaseModel, Field


class AccessRuleIdentifierRequest(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    layer: str = Field(
        alias="layer",
        description="""Layer that the rule belongs to identified by the name or UID.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
