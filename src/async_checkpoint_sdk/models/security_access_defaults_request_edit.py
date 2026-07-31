from .pydantic import BaseModel, Field


class SecurityAccessDefaultsRequestEdit(BaseModel):
    destination: str = Field(
        alias="destination",
        description="""Destination default value for new rule creation. Any or None.""",
    )
    service: str = Field(
        alias="service",
        description="""Service and Applications default value for new rule creation. Any or None.""",
    )
    source: str = Field(
        alias="source",
        description="""Source default value for new rule creation. Any or None.""",
    )
    track: str = Field(
        alias="track",
        description="""Track default value for new rule creation. Log or None.""",
    )
