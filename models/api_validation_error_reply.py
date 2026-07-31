from pydantic import BaseModel, Field


class ApiValidationErrorReply(BaseModel):
    message: str = Field(alias="message", description="""Operation status.""")
    warnings: list[dict] = Field(
        alias="warnings", description="""Validation warnings."""
    )
    errors: list[dict] = Field(alias="errors", description="""Validation errors.""")
    blocking_errors: list[dict] = Field(
        alias="blocking-errors", description="""Blocking validation errors."""
    )
    code: str = Field(alias="code", description="""Error code.""")
