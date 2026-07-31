from pydantic import BaseModel, Field


class SecurityZoneSettingsRequest(BaseModel):
    auto_calculated: bool = Field(
        alias="auto-calculated",
        description="""Security Zone is calculated according to where the interface leads to.""",
    )
