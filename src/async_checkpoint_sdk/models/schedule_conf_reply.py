from .day_recurrence_reply import DayRecurrenceReply
from .pydantic import BaseModel, Field


class ScheduleConfReply(BaseModel):
    time: str = Field(alias="time", description="""Time in format HH:mm.""")
    recurrence: DayRecurrenceReply = Field(alias="recurrence", description="""Days recurrence.""")
