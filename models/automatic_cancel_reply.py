from pydantic import BaseModel, Field


class AutomaticCancelReply(BaseModel):
    days: int = Field(
        alias="days", description="""Number of days to complete the upgrade."""
    )
    date: str = Field(
        alias="date",
        description="""Date and time to complete the upgrade in ISO 8601 format.""",
    )
    method: str = Field(alias="method", description="""Automatic cancel method.""")
