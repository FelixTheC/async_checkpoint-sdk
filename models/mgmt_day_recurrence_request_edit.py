from pydantic import BaseModel, Field


class MgmtDayRecurrenceRequestEdit(BaseModel):
    pattern: str = Field(alias="pattern", description="""Days recurrence pattern.""")
    weekdays: list[str] = Field(
        alias="weekdays",
        description="""Days of the week to run the update.<br> Valid values: group of values from {'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'}. <font color=red>Required only when</font> pattern is set to 'Weekly'.""",
    )
    days: list[str] = Field(
        alias="days",
        description="""Days of the month to run the update.<br> Valid values: interval in the range of 1 to 31. <font color=red>Required only when</font> pattern is set to 'Monthly'.""",
    )
