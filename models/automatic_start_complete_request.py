from pydantic import BaseModel, Field


class AutomaticStartCompleteRequest(BaseModel):
    enabled: bool = Field(
        alias="enabled",
        description="""Enable automatic completion of the background upgrade.""",
    )
    days: int = Field(
        alias="days",
        description="""Number of days to start 'Complete' phase. Default is 7 days.""",
    )
    date: str = Field(
        alias="date",
        description="""Date to start 'Complete' phase. Date format: YYYY-MM-DD.""",
    )
    method: str = Field(
        alias="method", description="""Automatic start method. Default is 'by-days'."""
    )
