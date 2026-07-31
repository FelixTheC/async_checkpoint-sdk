from api_date_reply import ApiDateReply
from gateways_onboard_settings_reply import GatewaysOnboardSettingsReply
from pydantic import BaseModel, Field


class CloudServicesStatusReply(BaseModel):
    status: str = Field(
        alias="status",
        description="""Status of the connection to the Infinity Portal.""",
    )
    connected_at: ApiDateReply = Field(
        alias="connected-at",
        description="""The time of the connection between the Management Server and the Infinity Portal.""",
    )
    management_url: str = Field(
        alias="management-url", description="""The Management Server's public URL."""
    )
    tenant_id: str = Field(
        alias="tenant-id", description="""Tenant ID of Infinity Portal."""
    )
    environment_id: str = Field(
        alias="environment-id",
        description="""The connected environment's ID in the Infinity Portal.""",
    )
    gateways_onboarding_settings: GatewaysOnboardSettingsReply = Field(
        alias="gateways-onboarding-settings",
        description="""Gateways on-boarding to Infinity Portal settings.""",
    )
