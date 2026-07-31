from .pydantic import BaseModel, Field


class PrvProfileRadiusReply(BaseModel):
    manage_settings: str = Field(
        alias="manage-settings",
        description="""Manage settings mode: locally on the device or centrally from .this application.""",
    )
    override_settings: str = Field(
        alias="override-settings",
        description="""Override settings mode: allowed, mandatory or denied. Relevant only when settings are managed centrally.""",
    )
    enabled: bool = Field(alias="enabled", description="""RADIUS enabled on device.""")
    radius_servers: list[dict] = Field(alias="radius-servers", description="""RADIUS Servers.""")
    allow_administrators_from_specific_radius_group_only: bool = Field(
        alias="allow-administrators-from-specific-radius-group-only",
        description="""Allow administrators from .specific radius group only.""",
    )
    allowed_radius_groups: list[str] = Field(
        alias="allowed-radius-groups", description="""Allowed radius groups."""
    )
