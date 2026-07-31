from pydantic import BaseModel, Field


class SetHaStateRequest(BaseModel):
    new_state: str = Field(alias="new-state", description="""Domain server new state.""")
    ignore_errors: bool = Field(
        alias="ignore-errors", description="""Apply changes ignoring errors."""
    )
