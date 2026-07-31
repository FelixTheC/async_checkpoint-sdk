from pydantic import BaseModel, Field


class AutomaticCancelRequest(BaseModel):
    days: int = Field(
        alias="days", description="""Number of days to complete the upgrade. Default is 10 days."""
    )
    date: str = Field(
        alias="date", description="""Date to complete the upgrade. Date format: YYYY-MM-DD."""
    )
    method: str = Field(
        alias="method", description="""Automatic cancel method. Default is 'by-days'."""
    )
