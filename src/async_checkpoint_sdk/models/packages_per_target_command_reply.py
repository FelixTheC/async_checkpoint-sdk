from .pydantic import BaseModel, Field


class PackagesPerTargetCommandReply(BaseModel):
    source: int = Field(
        alias="from", description="""from .which element number the query was done."""
    )
    targets: list[dict] = Field(
        alias="targets",
        description="""The target objects. Target objects can be Security Gateways or Clusters.""",
    )
    to: int = Field(alias="to", description="""To which element number the query was done.""")
    total: int = Field(
        alias="total", description="""Total number of elements returned by the query."""
    )
