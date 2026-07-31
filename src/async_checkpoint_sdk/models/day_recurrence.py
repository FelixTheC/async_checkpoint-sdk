from .pydantic import BaseModel, Field


class DayRecurrence(BaseModel):
    days: list[str] = Field(
        alias="days",
        description="""Valid on specific days. Multiple options, support range of days in months. Example:[1,3,9-20].""",
    )
    month: str = Field(alias="month", description="""Valid on month. Example: 1, 2,12,Any.""")
    pattern: str = Field(alias="pattern", description="""Valid on Daily, Weekly, Monthly base.""")
    weekdays: list[str] = Field(
        alias="weekdays", description="""Valid on weekdays. Example: Sun, Mon...Sat."""
    )
