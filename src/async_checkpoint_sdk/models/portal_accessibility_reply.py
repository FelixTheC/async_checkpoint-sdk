from internal_access_reply import InternalAccessReply
from pydantic import BaseModel, Field


class PortalAccessibilityReply(BaseModel):
    allow_access_from: str = Field(
        alias="allow-access-from",
        description="""Allowed access to the web portal (based on interfaces, or security policy).""",
    )
    internal_access_settings: InternalAccessReply = Field(
        alias="internal-access-settings",
        description="""Configuration of the additional portal access settings for internal interfaces only.""",
    )
