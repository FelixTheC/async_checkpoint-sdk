from auth_settings_browser_based_edit import AuthSettingsBrowserBasedEdit
from browser_based_auth_portal_api_edit import BrowserBasedAuthPortalApiEdit
from pydantic import BaseModel, Field


class BrowserBasedAuthSettingsEdit(BaseModel):
    authentication_settings: AuthSettingsBrowserBasedEdit = Field(
        alias="authentication-settings",
        description="""Authentication Settings for Browser Based Authentication.""",
    )
    browser_based_authentication_portal_settings: BrowserBasedAuthPortalApiEdit = Field(
        alias="browser-based-authentication-portal-settings",
        description="""Browser Based Authentication portal settings.""",
    )
