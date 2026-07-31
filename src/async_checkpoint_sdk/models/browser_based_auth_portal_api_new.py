from .certificate_settings_request import CertificateSettingsRequest
from .portal_accessibility_request import PortalAccessibilityRequest
from .portal_web_settings_request_new import PortalWebSettingsRequestNew
from .pydantic import BaseModel, Field


class BrowserBasedAuthPortalApiNew(BaseModel):
    portal_web_settings: PortalWebSettingsRequestNew = Field(
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
