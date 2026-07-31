from .api_date_reply import ApiDateReply
from .login_message_reply import LoginMessageReply
from .pydantic import BaseModel, Field


class WebApiLoginReply(BaseModel):
    sid: str = Field(
        alias="sid",
        description="""Session unique identifier. Enter this session unique identifier in the 'X-chkp-sid' header of each request.""",
    )
    api_server_version: str = Field(
        alias="api-server-version", description="""API Server version."""
    )
    background_upgrade_message: str = Field(
        alias="background-upgrade-message",
        description="""Displayed when the management server is undergoing a background upgrade.""",
    )
    disk_space_message: str = Field(
        alias="disk-space-message",
        description="""Information about the available disk space on the management server.""",
    )
    last_login_was_at: ApiDateReply = Field(
        alias="last-login-was-at",
        description="""Timestamp when administrator last accessed the management server.""",
    )
    login_message: LoginMessageReply = Field(
        alias="login-message", description="""Login message."""
    )
    read_only: bool = Field(alias="read-only", description="""True if this session is read only.""")
    session_timeout: int = Field(
        alias="session-timeout",
        description="""Session expiration timeout in seconds.""",
    )
    standby: bool = Field(
        alias="standby",
        description="""True if this management server is in the standby mode.""",
    )
    uid: str = Field(
        alias="uid",
        description="""Session object unique identifier. This identifier may be used in the discard API to discard changes that were made in this session, when administrator is working from .another session, or in the 'switch-session' API.""",
    )
    url: str = Field(alias="url", description="""URL that was used to reach the API server.""")
