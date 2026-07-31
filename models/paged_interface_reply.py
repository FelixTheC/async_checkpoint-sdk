from pydantic import BaseModel, Field


class PagedInterfaceReply(BaseModel):
    source: int = Field(
        alias="from", description="""From which element number the query was done."""
    )
    objects: list[dict] = Field(
        alias="objects", description="""Cluster network interfaces list."""
    )
    to: int = Field(
        alias="to", description="""To which element number the query was done."""
    )
    total: int = Field(
        alias="total", description="""Total number of elements returned by the query."""
    )
