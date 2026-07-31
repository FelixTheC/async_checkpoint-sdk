from pydantic import BaseModel, Field


class TaskQueryReply(BaseModel):
    source: int = Field(
        alias="from", description="""From which element number the query was done."""
    )
    tasks: list[dict] = Field(
        alias="tasks",
        description="""How much details are returned depends on the details-level field of the request. This table shows the level of detail shown when details-level is set to full.""",
    )
    to: int = Field(
        alias="to", description="""To which element number the query was done."""
    )
    total: int = Field(
        alias="total", description="""Total number of elements returned by the query."""
    )
