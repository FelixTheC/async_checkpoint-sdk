from pydantic import BaseModel, Field


class IndicatorOverrideRequest(BaseModel):
    action: str = Field(alias="action", description="""The indicator's action in this profile.""")
    profile: str = Field(
        alias="profile", description="""The profile in which to override the indicator's action."""
    )
