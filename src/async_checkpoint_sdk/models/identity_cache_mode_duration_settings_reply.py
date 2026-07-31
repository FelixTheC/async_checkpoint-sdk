from pydantic import BaseModel, Field


class IdentityCacheModeDurationSettingsReply(BaseModel):
    override_profile: bool = Field(
        alias="override-profile", description="""Override profile of global configuration."""
    )
    profile_value: int = Field(alias="profile-value", description="""Override profile value.""")
    value: int = Field(alias="value", description="""Override value.""")
