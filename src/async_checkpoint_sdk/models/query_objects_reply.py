from pydantic import BaseModel, Field


class QueryObjectsReply(BaseModel):
    from_: int = Field(
        alias="from", description="""From which element number the query was done."""
    )
    objects: list[dict] = Field(
        alias="objects",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level. In case of details-level is set to full, all unsupported objects will be shown with a warning saying that the response could change when support for these object is added.""",
    )
    to: int = Field(alias="to", description="""To which element number the query was done.""")
    total: int = Field(
        alias="total", description="""Total number of elements returned by the query."""
    )
