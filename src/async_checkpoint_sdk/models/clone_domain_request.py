from .pydantic import BaseModel, Field


class CloneDomainRequest(BaseModel):
    omit_sensitive_info: bool = Field(
        alias="omit-sensitive-info",
        description="""Remove sensitive information from .exported database.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings",
        description="""Ignoring the verification warnings. By Setting this parameter to 'true' the clone will not be blocked by warnings.""",
    )
