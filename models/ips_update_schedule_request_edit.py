from ips_update_schedule_day_recurrence import IpsUpdateScheduleDayRecurrence
from pydantic import BaseModel, Field


class IpsUpdateScheduleRequestEdit(BaseModel):
    enabled: bool = Field(
        alias="enabled", description="""Enable/Disable IPS Update Schedule."""
    )
    time: str = Field(alias="time", description="""Time in format HH:mm.""")
    recurrence: IpsUpdateScheduleDayRecurrence = Field(
        alias="recurrence", description="""Days recurrence."""
    )
