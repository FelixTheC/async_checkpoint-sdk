from .pydantic import BaseModel, Field


class TrustRequestBase(BaseModel):
    trust_method: str = Field(
        alias="trust-method",
        description="""Trust method to use for establishing communication.""",
    )
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from .the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
    )
