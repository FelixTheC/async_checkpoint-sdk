from pydantic import BaseModel, Field


class QueryNatRulebaseReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    source: int = Field(
        alias="from", description="""From which element number the query was done."""
    )
    objects_dictionary: list[dict] = Field(
        alias="objects-dictionary",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    rulebase: list[dict] = Field(alias="rulebase", description="""N/A""")
    to: int = Field(
        alias="to", description="""To which element number the query was done."""
    )
    total: int = Field(
        alias="total", description="""Total number of elements returned by the query."""
    )
