from .pydantic import BaseModel, Field


class AutomaticPurgeRecurrenceRequest(BaseModel):
    start_date: str = Field(
        alias="start-date",
        description="""The first time to check whether or not there are sessions to purge. ISO 8601. If timezone isn't specified in the input, the Management server's timezone is used. Instead - If you want to start immediately, type: now. Note: when the automatic purge feature is enabled, this field must be set.""",
    )
    time_units: str = Field(
        alias="time-units",
        description="""Note: when the automatic purge feature is enabled, this field must be set.""",
    )
    check_interval: int = Field(
        alias="check-interval",
        description="""Number of time-units between two purge checks.  Note: when the automatic purge feature is enabled, this field must be set.""",
    )
