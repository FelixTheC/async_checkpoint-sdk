from .automatic_purge_recurrence_reply import AutomaticPurgeRecurrenceReply
from .pydantic import BaseModel, Field


class AutomaticPurgeReply(BaseModel):
    enabled: bool = Field(
        alias="enabled", description="""Turn on/off the automatic-purge feature."""
    )
    keep_sessions_by_count: bool = Field(
        alias="keep-sessions-by-count",
        description="""Whether or not to keep the latest N sessions.""",
    )
    number_of_sessions_to_keep: int = Field(
        alias="number-of-sessions-to-keep",
        description="""The number of newest sessions to preserve, by the sessions's publish date.""",
    )
    keep_sessions_by_days: bool = Field(
        alias="keep-sessions-by-days",
        description="""Whether or not to keep the sessions for D days.""",
    )
    number_of_days_to_keep: int = Field(
        alias="number-of-days-to-keep",
        description="""When keep-sessions-by-days = true this sets the number of days to keep the sessions.""",
    )
    scheduling: AutomaticPurgeRecurrenceReply = Field(
        alias="scheduling",
        description="""When to purge sessions that do not meet the keep criteria.""",
    )
