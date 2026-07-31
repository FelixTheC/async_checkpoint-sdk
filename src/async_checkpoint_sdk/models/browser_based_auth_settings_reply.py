from .auth_settings_browser_based_reply import AuthSettingsBrowserBasedReply
from .i_d_a_portal_reply import IDAPortalReply
from .pydantic import BaseModel, Field


class BrowserBasedAuthSettingsReply(BaseModel):
    authentication_settings: AuthSettingsBrowserBasedReply = Field(
        alias="authentication-settings", description="""N/A"""
    )
    browser_based_authentication_portal_settings: IDAPortalReply = Field(
        alias="browser-based-authentication-portal-settings",
        description="""Browser Based Authentication portal settings.""",
    )
