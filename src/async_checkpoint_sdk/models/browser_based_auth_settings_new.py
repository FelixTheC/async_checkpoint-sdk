from .auth_settings_browser_based_new import AuthSettingsBrowserBasedNew
from .browser_based_auth_portal_api_new import BrowserBasedAuthPortalApiNew
from .pydantic import BaseModel, Field


class BrowserBasedAuthSettingsNew(BaseModel):
    authentication_settings: AuthSettingsBrowserBasedNew = Field(
        alias="authentication-settings",
        description="""Authentication Settings for Browser Based Authentication.""",
    )
    browser_based_authentication_portal_settings: BrowserBasedAuthPortalApiNew = Field(
        alias="browser-based-authentication-portal-settings",
        description="""Browser Based Authentication portal settings.""",
    )
