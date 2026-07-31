from .pydantic import BaseModel, Field


class LsmClusterMemberProvisioningSettingsReply(BaseModel):
    provisioning_profile: str = Field(
        alias="provisioning-profile", description="""Attached provisioning profile."""
    )
