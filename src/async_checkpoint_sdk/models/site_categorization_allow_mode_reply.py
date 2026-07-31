from .pydantic import BaseModel, Field


class SiteCategorizationAllowModeReply(BaseModel):
    override_profile: bool = Field(
        alias="override-profile",
        description="""Override profile of global configuration.""",
    )
    profile_value: str = Field(alias="profile-value", description="""Override profile value.""")
    value: str = Field(alias="value", description="""Override value.""")
