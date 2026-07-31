from .pydantic import BaseModel, Field


class SecurityZoneSettingsReply(BaseModel):
    auto_calculated: bool = Field(
        alias="auto-calculated",
        description="""Security Zone is calculated according to where the interface leads to.""",
    )
    auto_calculated_zone: str = Field(alias="auto-calculated-zone", description="""N/A""")
    auto_calculated_zone_uid: str = Field(alias="auto-calculated-zone-uid", description="""N/A""")
    specific_security_zone_enabled: bool = Field(
        alias="specific-security-zone-enabled", description="""N/A"""
    )
    specific_zone: str = Field(
        alias="specific-zone", description="""Security Zone specified manually."""
    )
    specific_zone_uid: str = Field(alias="specific-zone-uid", description="""N/A""")
