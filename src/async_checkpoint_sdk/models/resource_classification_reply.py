from custom_settings_reply import CustomSettingsReply
from pydantic import BaseModel, Field


class ResourceClassificationReply(BaseModel):
    custom_settings: CustomSettingsReply = Field(
        alias="custom-settings", description="""Custom resources classification per service."""
    )
    mode: str = Field(
        alias="mode", description="""Set all services to the same mode or choose a custom mode."""
    )
    web_service_fail_mode: str = Field(
        alias="web-service-fail-mode",
        description="""Block connections when the web service is unavailable.""",
    )
