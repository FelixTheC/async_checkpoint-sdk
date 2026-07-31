from pydantic import BaseModel, Field


class ProfileIndicatorOverrideRequest(BaseModel):
    action: str = Field(
        alias="action", description="""The indicator's action in this profile."""
    )
    indicator: str = Field(
        alias="indicator",
        description="""The indicator whose action is to be overriden.""",
    )
