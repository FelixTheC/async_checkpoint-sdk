from .pydantic import BaseModel, Field


class IpsUpdateScheduleDayRecurrence(BaseModel):
    days: list[str] = Field(
        alias="days",
        description="""Valid on specific days. Multiple options, support range of days in months. Example:[1,3,9-20].""",
    )
    minutes: int = Field(
        alias="minutes",
        description="""Valid on interval. The length of time in minutes between updates.""",
    )
    pattern: str = Field(
        alias="pattern",
        description="""Valid on Interval, Daily, Weekly, Monthly base.""",
    )
    weekdays: list[str] = Field(
        alias="weekdays", description="""Valid on weekdays. Example: Sun, Mon...Sat."""
    )
