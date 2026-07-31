from pydantic import BaseModel, Field


class PrvProfileHotspotReply(BaseModel):
    manage_settings: str = Field(
        alias="manage-settings",
        description="""Manage settings mode: locally on the device or centrally from this application.""",
    )
    override_settings: str = Field(
        alias="override-settings",
        description="""Override settings mode: allowed, mandatory or denied. Relevant only when settings are managed centrally.""",
    )
    enabled: bool = Field(alias="enabled", description="""Hotspot enabled on device.""")
    portal_title: str = Field(alias="portal-title", description="""Portal title.""")
    portal_message: str = Field(alias="portal-message", description="""Portal message.""")
    display_terms_of_use: bool = Field(
        alias="display-terms-of-use", description="""Use terms of use."""
    )
    terms_of_use: str = Field(alias="terms-of-use", description="""Terms of use.""")
    require_authentication: bool = Field(
        alias="require-authentication", description="""Require authentication."""
    )
    allow_users_from_specific_group: bool = Field(
        alias="allow-users-from-specific-group", description="""Allow users from specific group."""
    )
    allowed_users_groups: list[str] = Field(
        alias="allowed-users-groups", description="""Allowed users groups."""
    )
