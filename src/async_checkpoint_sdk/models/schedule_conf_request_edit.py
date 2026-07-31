from .day_recurrence_request_edit import DayRecurrenceRequestEdit
from .pydantic import BaseModel, Field


class ScheduleConfRequestEdit(BaseModel):
    time: str = Field(alias="time", description="""Time in format HH:mm.""")
    recurrence: DayRecurrenceRequestEdit = Field(
        alias="recurrence", description="""Days recurrence."""
    )
