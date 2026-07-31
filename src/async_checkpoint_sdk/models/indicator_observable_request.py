from pydantic import BaseModel, Field


class IndicatorObservableRequest(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    md5: str = Field(alias="md5", description="""A valid MD5 sequence.""")
    confidence: str = Field(
        alias="confidence",
        description="""The confidence level the indicator has that a real threat has been uncovered.""",
    )
    product: str = Field(
        alias="product",
        description="""The software blade that processes the observable: AV - AntiVirus, AB - AntiBot.""",
    )
    severity: str = Field(alias="severity", description="""The severity level of the threat.""")
    comments: str = Field(alias="comments", description="""Comments string.""")
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
