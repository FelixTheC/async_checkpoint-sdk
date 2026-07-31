from gateways_onboard_settings_request_connect import (
    GatewaysOnboardSettingsRequestConnect,
)
from pydantic import BaseModel, Field


class CloudConnectMgmtRequest(BaseModel):
    gateways_onboarding_settings: GatewaysOnboardSettingsRequestConnect = Field(
        alias="gateways-onboarding-settings",
        description="""Gateways on-boarding to Infinity Portal settings.""",
    )
