from .pydantic import BaseModel, Field


class AutomaticPurgeRecurrenceReply(BaseModel):
    start_date: str = Field(
        alias="start-date",
        description="""The first time to check whether or not there are sessions to purge.""",
    )
    time_units: str = Field(alias="time-units", description="""N/A""")
    check_interval: int = Field(
        alias="check-interval",
        description="""Number of time-units between two purge checks.""",
    )
    last_check: str = Field(
        alias="last-check", description="""Last time purge check was executed."""
    )
    next_check: str = Field(
        alias="next-check", description="""Next time purge check will be executed."""
    )
