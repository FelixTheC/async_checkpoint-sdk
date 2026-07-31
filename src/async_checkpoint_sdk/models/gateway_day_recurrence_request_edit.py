from pydantic import BaseModel, Field


class GatewayDayRecurrenceRequestEdit(BaseModel):
    pattern: str = Field(alias="pattern", description="""Days recurrence pattern.""")
    interval_hours: int = Field(
        alias="interval-hours",
        description="""The amount of hours between updates. <font color=red>Required only when</font> pattern is set to 'Interval'.""",
    )
    interval_minutes: int = Field(
        alias="interval-minutes",
        description="""The amount of minutes between updates. <font color=red>Required only when</font> pattern is set to 'Interval'.""",
    )
    interval_seconds: int = Field(
        alias="interval-seconds",
        description="""The amount of seconds between updates. <font color=red>Required only when</font> pattern is set to 'Interval'.""",
    )
    weekdays: list[str] = Field(
        alias="weekdays",
        description="""Days of the week to run the update.<br> Valid values: group of values from {'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'}. <font color=red>Required only when</font> pattern is set to 'Weekly'.""",
    )
    days: list[str] = Field(
        alias="days",
        description="""Days of the month to run the update.<br> Valid values: interval in the range of 1 to 31. <font color=red>Required only when</font> pattern is set to 'Monthly'.""",
    )
