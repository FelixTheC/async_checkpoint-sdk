from .pydantic import BaseModel, Field


class LsmGatewayProvisioningSettingsReply(BaseModel):
    provisioning_profile: str = Field(
        alias="provisioning-profile", description="""Attached provisioning profile."""
    )
