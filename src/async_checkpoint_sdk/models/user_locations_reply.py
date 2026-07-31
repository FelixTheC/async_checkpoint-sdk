from .pydantic import BaseModel, Field


class UserLocationsReply(BaseModel):
    destinations: list[dict] = Field(
        alias="destinations",
        description="""Collection of allowed destination location uid. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    sources: list[dict] = Field(
        alias="sources",
        description="""Collection of allowed source location uid. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
