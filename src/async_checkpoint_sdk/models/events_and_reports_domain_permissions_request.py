from pydantic import BaseModel, Field


class EventsAndReportsDomainPermissionsRequest(BaseModel):
    smart_event: str = Field(
        alias="smart-event", description="""'Custom' - Configure SmartEvent permissions."""
    )
    events: str = Field(
        alias="events",
        description="""Work with event queries on the Events tab. Create custom event queries.<br>Available only if smart-event is set to 'Custom'.""",
    )
    policy: str = Field(
        alias="policy",
        description="""Configure SmartEvent Policy rules and install SmartEvent Policies.<br>Available only if smart-event is set to 'Custom'.""",
    )
    reports: bool = Field(
        alias="reports",
        description="""Create and run SmartEvent reports.<br>Available only if smart-event is set to 'Custom'.""",
    )
