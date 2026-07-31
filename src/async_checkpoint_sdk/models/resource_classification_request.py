from custom_settings_request import CustomSettingsRequest
from pydantic import BaseModel, Field


class ResourceClassificationRequest(BaseModel):
    custom_settings: CustomSettingsRequest = Field(
        alias="custom-settings",
        description="""On Custom mode, custom resources classification per service.""",
    )
    mode: str = Field(
        alias="mode", description="""Set all services to the same mode or choose a custom mode."""
    )
    web_service_fail_mode: str = Field(
        alias="web-service-fail-mode",
        description="""Block connections when the web service is unavailable.""",
    )
