from .mgmt_day_recurrence_reply import MgmtDayRecurrenceReply
from .pydantic import BaseModel, Field


class ScheduleConfMgmtReply(BaseModel):
    time: str = Field(alias="time", description="""Time in format HH:mm.""")
    recurrence: MgmtDayRecurrenceReply = Field(
        alias="recurrence", description="""Days recurrence."""
    )
