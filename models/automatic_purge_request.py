from automatic_purge_recurrence_request import AutomaticPurgeRecurrenceRequest
from pydantic import BaseModel, Field


class AutomaticPurgeRequest(BaseModel):
    keep_sessions_by_count: bool = Field(
        alias="keep-sessions-by-count",
        description="""Whether or not to keep the latest N sessions.
Note: when the automatic purge feature is enabled, this field and/or the keep-sessions-by-date field must be set to 'true'.""",
    )
    number_of_sessions_to_keep: int = Field(
        alias="number-of-sessions-to-keep",
        description="""When keep-sessions-by-count = true this sets the number of newest sessions to preserve, by the sessions's publish date.""",
    )
    keep_sessions_by_days: bool = Field(
        alias="keep-sessions-by-days",
        description="""Whether or not to keep the sessions for D days.
Note: when the automatic purge feature is enabled, this field and/or the keep-sessions-by-count field must be set to 'true'.""",
    )
    number_of_days_to_keep: int = Field(
        alias="number-of-days-to-keep",
        description="""When keep-sessions-by-days = true this sets the number of days to keep the sessions.""",
    )
    scheduling: AutomaticPurgeRecurrenceRequest = Field(
        alias="scheduling",
        description="""When to purge sessions that do not meet the keep criteria. Note: when the automatic purge feature is enabled, this field must be set.""",
    )
