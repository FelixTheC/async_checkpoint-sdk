from .certificate_settings_request import CertificateSettingsRequest
from .portal_accessibility_request import PortalAccessibilityRequest
from .portal_web_settings_request import PortalWebSettingsRequest
from .pydantic import BaseModel, Field


class UserCheckPortalRequest(BaseModel):
    enabled: bool = Field(
        alias="enabled",
        description="""State of the web portal (enabled or disabled). The supported blades are: {'Application Control', 'URL Filtering', 'Data Loss Prevention', 'Anti Virus', 'Anti Bot', 'Threat Emulation', 'Threat Extraction', 'Data Awareness'}.""",
    )
    portal_web_settings: PortalWebSettingsRequest = Field(
        alias="portal-web-settings",
        description="""Configuration of the portal web settings.""",
    )
    certificate_settings: CertificateSettingsRequest = Field(
        alias="certificate-settings",
        description="""Configuration of the portal certificate settings.""",
    )
    accessibility: PortalAccessibilityRequest = Field(
        alias="accessibility",
        description="""Configuration of the portal access settings.""",
    )
