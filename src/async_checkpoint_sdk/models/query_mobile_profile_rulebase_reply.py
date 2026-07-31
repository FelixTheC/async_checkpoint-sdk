from .pydantic import BaseModel, Field


class QueryMobileProfileRulebaseReply(BaseModel):
    source: int = Field(
        alias="from", description="""from .which element number the query was done."""
    )
    rulebase: list[dict] = Field(
        alias="rulebase", description="""The entire Mobile Profile Rules."""
    )
    to: int = Field(alias="to", description="""To which element number the query was done.""")
    total: int = Field(
        alias="total", description="""Total number of elements returned by the query."""
    )
