from pydantic import BaseModel, Field


class PackagesQueryReply(BaseModel):
    source: int = Field(
        alias="from", description="""From which element number the query was done."""
    )
    packages: list[dict] = Field(
        alias="packages",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    to: int = Field(
        alias="to", description="""To which element number the query was done."""
    )
    total: int = Field(
        alias="total", description="""Total number of elements returned by the query."""
    )
