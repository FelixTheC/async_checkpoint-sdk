from .gateway_day_recurrence_reply import GatewayDayRecurrenceReply
from .pydantic import BaseModel, Field


class ScheduleConfGatewayReply(BaseModel):
    time: str = Field(alias="time", description="""Time in format HH:mm.""")
    recurrence: GatewayDayRecurrenceReply = Field(
        alias="recurrence", description="""Days recurrence."""
    )
