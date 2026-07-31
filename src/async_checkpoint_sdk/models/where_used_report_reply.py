from pydantic import BaseModel, Field


class WhereUsedReportReply(BaseModel):
    total: int = Field(alias="total", description="""Total usage number.""")
    objects: list[dict] = Field(
        alias="objects",
        description="""Usage in objects.
Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    access_control_rules: list[dict] = Field(
        alias="access-control-rules",
        description="""Usage in Access Control Policy rules.
Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    nat_rules: list[dict] = Field(
        alias="nat-rules",
        description="""Usage in Network Address Translation Policy rules.
Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    threat_prevention_rules: list[dict] = Field(
        alias="threat-prevention-rules",
        description="""Usage in Threat Prevention Policy rules.
Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    https_rules: list[dict] = Field(
        alias="https-rules",
        description="""Usage in HTTPS Policy rules.
Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
