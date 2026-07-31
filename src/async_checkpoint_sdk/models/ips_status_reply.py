from api_date_reply import ApiDateReply
from pydantic import BaseModel, Field


class IpsStatusReply(BaseModel):
    installed_version: str = Field(
        alias="installed-version", description="""Installed IPS version."""
    )
    installed_version_creation_time: ApiDateReply = Field(
        alias="installed-version-creation-time",
        description="""Installed IPS version creation time.""",
    )
    last_updated: ApiDateReply = Field(
        alias="last-updated",
        description="""When IPS was updated on the management server for the last time.""",
    )
    latest_version: str = Field(
        alias="latest-version", description="""Latest IPS version available on User Center."""
    )
    latest_version_creation_time: ApiDateReply = Field(
        alias="latest-version-creation-time", description="""Latest IPS version creation time."""
    )
    update_available: bool = Field(
        alias="update-available", description="""Is IPS update available."""
    )
