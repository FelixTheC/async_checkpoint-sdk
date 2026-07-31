from pydantic import BaseModel, Field


class IdentityCacheModeSettingsReply(BaseModel):
    override_profile: bool = Field(
        alias="override-profile", description="""Override profile of global configuration."""
    )
    profile_value: bool = Field(alias="profile-value", description="""Override profile value.""")
    value: bool = Field(alias="value", description="""Override value.""")
