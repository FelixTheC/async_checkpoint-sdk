from api_date_reply import ApiDateReply
from date import Date
from pydantic import BaseModel, Field


class TrustedCaStatusReply(BaseModel):
    connection_status: str = Field(
        alias="connection-status",
        description="""The status of the connection to the download center.""",
    )
    installed_version: str = Field(
        alias="installed-version", description="""Currently installed version."""
    )
    last_checked: ApiDateReply = Field(
        alias="last-checked",
        description="""The last time the updated Trusted CAs package was checked.""",
    )
    last_updated: ApiDateReply = Field(
        alias="last-updated",
        description="""When the Trusted CAs package was updated for the last time.""",
    )
    latest_version: str = Field(
        alias="latest-version", description="""Latest available version."""
    )
    latest_version_creation_time: Date = Field(
        alias="latest-version-creation-time",
        description="""Latest Trusted CAs package creation time.""",
    )
    update_available: bool = Field(
        alias="update-available", description="""Is update available."""
    )
