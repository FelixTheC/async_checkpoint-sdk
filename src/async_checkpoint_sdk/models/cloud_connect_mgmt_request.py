from gateways_onboard_settings_request_connect import GatewaysOnboardSettingsRequestConnect
from pydantic import BaseModel, Field


class CloudConnectMgmtRequest(BaseModel):
    auth_token: str = Field(
        alias="auth-token",
        description="""Copy the authentication token from the Smart-1 cloud service hosted in the Infinity Portal.""",
    )
    gateways_onboarding_settings: GatewaysOnboardSettingsRequestConnect = Field(
        alias="gateways-onboarding-settings",
        description="""Gateways on-boarding to Infinity Portal settings.""",
    )
