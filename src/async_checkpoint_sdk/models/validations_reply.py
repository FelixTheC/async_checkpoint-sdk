from .pydantic import BaseModel, Field


class ValidationsReply(BaseModel):
    warnings: list[dict] = Field(alias="warnings", description="""Validation warnings.""")
    warnings_total: int = Field(
        alias="warnings-total", description="""Total number of warning validations."""
    )
    errors: list[dict] = Field(alias="errors", description="""Validation errors.""")
    errors_total: int = Field(
        alias="errors-total", description="""Total number of error validations."""
    )
    blocking_errors: list[dict] = Field(
        alias="blocking-errors", description="""Blocking validation errors."""
    )
    blocking_errors_total: int = Field(
        alias="blocking-errors-total",
        description="""Total number of blocking error validations.""",
    )
