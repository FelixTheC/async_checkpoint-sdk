from .mgmt_day_recurrence_request_edit import MgmtDayRecurrenceRequestEdit
from .pydantic import BaseModel, Field


class ScheduleConfMgmtRequestEdit(BaseModel):
    time: str = Field(alias="time", description="""Time in format HH:mm.""")
    recurrence: MgmtDayRecurrenceRequestEdit = Field(
        alias="recurrence", description="""Days recurrence."""
    )
