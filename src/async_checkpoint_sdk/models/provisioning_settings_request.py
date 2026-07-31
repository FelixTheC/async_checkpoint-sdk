from .pydantic import BaseModel, Field


class ProvisioningSettingsRequest(BaseModel):
    provisioning_profile: str = Field(
        alias="provisioning-profile", description="""Provisioning profile."""
    )
