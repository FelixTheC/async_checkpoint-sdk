from pydantic import BaseModel, Field


class AutomaticStartCompleteReply(BaseModel):
    enabled: bool = Field(
        alias="enabled", description="""Enable automatic start of background upgrade."""
    )
    days: int = Field(alias="days", description="""Number of days to start background upgrade.""")
    date: str = Field(
        alias="date",
        description="""Date and time to start background upgrade in ISO 8601 format.""",
    )
    method: str = Field(alias="method", description="""Automatic start method.""")
