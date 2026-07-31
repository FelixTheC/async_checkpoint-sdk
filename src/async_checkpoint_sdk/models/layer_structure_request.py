from pydantic import BaseModel, Field


class LayerStructureRequest(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    package: str = Field(
        alias="package",
        description="""Name of the package. Must be set when want to receive the resolved rule instead of the place holder in global domain layer.""",
    )
    limit: int = Field(alias="limit", description="""The maximal number of returned results.""")
    offset: int = Field(alias="offset", description="""Number of the results to initially skip.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
