from .pydantic import BaseModel, Field


class HourRange(BaseModel):
    enabled: bool = Field(alias="enabled", description="""Is hour range enabled.""")
    source: str = Field(alias="from", description="""Time in format HH:MM.""")
    index: int = Field(
        alias="index", description="""Hour range index. Must be unique in the list."""
    )
    to: str = Field(alias="to", description="""Time in format HH:MM.""")
