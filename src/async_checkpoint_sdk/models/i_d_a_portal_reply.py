from certificate_settings_reply import CertificateSettingsReply
from portal_accessibility_reply import PortalAccessibilityReply
from portal_web_settings_reply import PortalWebSettingsReply
from pydantic import BaseModel, Field


class IDAPortalReply(BaseModel):
    portal_web_settings: PortalWebSettingsReply = Field(
        alias="portal-web-settings", description="""Configuration of the portal web settings."""
    )
    certificate_settings: CertificateSettingsReply = Field(
        alias="certificate-settings",
        description="""Configuration of the portal certificate settings
Relevant only for non default certificate.""",
    )
    accessibility: PortalAccessibilityReply = Field(
        alias="accessibility", description="""Configuration of the portal access settings."""
    )
