from gateways_onboard_settings_request_edit import GatewaysOnboardSettingsRequestEdit
from pydantic import BaseModel, Field


class CloudServicesRequestEdit(BaseModel):
    gateways_onboarding_settings: GatewaysOnboardSettingsRequestEdit = Field(
        alias="gateways-onboarding-settings",
        description="""Gateways on-boarding to Infinity Portal settings.""",
    )
    status: str = Field(alias="status", description="""Connection status.""")
