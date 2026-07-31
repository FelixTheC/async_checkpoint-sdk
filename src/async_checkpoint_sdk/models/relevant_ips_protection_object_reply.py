from pydantic import BaseModel, Field


class RelevantIpsProtectionObjectReply(BaseModel):
    action: str = Field(
        alias="action", description="""The current action of the Threat Prevention profile."""
    )
    enabled: bool = Field(
        alias="enabled",
        description="""Shows if the Compliance scan is enabled or not for this object.""",
    )
    profile_name: str = Field(
        alias="profile-name", description="""The name of the relevant Threat Prevention profile."""
    )
    profile_uid: str = Field(
        alias="profile-uid", description="""The UID of the relevant Threat Prevention profile."""
    )
    protection_name: str = Field(
        alias="protection-name", description="""The name of the relevant IPS protection."""
    )
    status: str = Field(alias="status", description="""The status of the relevant object.""")
