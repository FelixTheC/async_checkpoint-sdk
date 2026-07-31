from gateway_day_recurrence_request_edit import GatewayDayRecurrenceRequestEdit
from pydantic import BaseModel, Field


class ScheduleConfGatewayRequestEdit(BaseModel):
    time: str = Field(alias="time", description="""Time in format HH:mm.""")
    recurrence: GatewayDayRecurrenceRequestEdit = Field(
        alias="recurrence", description="""Days recurrence."""
    )
