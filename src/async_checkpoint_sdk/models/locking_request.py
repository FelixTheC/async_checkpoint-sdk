from pydantic import BaseModel, Field


class LockingRequest(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    type: str = Field(alias="type", description="""Object type.""")
    layer: str = Field(
        alias="layer",
        description="""Object layer, need to specify the layer if the object is rule/section and uid is not supplied.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
