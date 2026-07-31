from api_domain_identifier import ApiDomainIdentifier
from ips_update_schedule_day_recurrence import IpsUpdateScheduleDayRecurrence
from pydantic import BaseModel, Field


class IpsUpdateScheduleReply(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    enabled: bool = Field(
        alias="enabled", description="""IPS Update Schedule status."""
    )
    type: str = Field(alias="type", description="""Object type.""")
    time: str = Field(alias="time", description="""Time in format HH:mm.""")
    recurrence: IpsUpdateScheduleDayRecurrence = Field(
        alias="recurrence", description="""Days recurrence."""
    )
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
