from .pydantic import BaseModel, Field


class QueryGatewaysServersReply(BaseModel):
    source: int = Field(
        alias="from", description="""from .which element number the query was done."""
    )
    to: int = Field(alias="to", description="""To which element number the query was done.""")
    total: int = Field(
        alias="total", description="""Total number of elements returned by the query."""
    )
    objects: list[dict] = Field(
        alias="objects",
        description="""How much detail is returned depends on the detail-level field of the request. This table shows the level of detail shown when details-level is set to full.""",
    )
