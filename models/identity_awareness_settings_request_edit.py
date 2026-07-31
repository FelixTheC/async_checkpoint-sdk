from browser_based_auth_settings_edit import BrowserBasedAuthSettingsEdit
from ida_proxy_settings_edit import IdaProxySettingsEdit
from identity_agent_settings_edit import IdentityAgentSettingsEdit
from identity_collector_settings_edit import IdentityCollectorSettingsEdit
from identity_sharing_settings_edit import IdentitySharingSettingsEdit
from identity_web_api_settings_edit import IdentityWebApiSettingsEdit
from pydantic import BaseModel, Field


class IdentityAwarenessSettingsRequestEdit(BaseModel):
    browser_based_authentication: bool = Field(
        alias="browser-based-authentication",
        description="""Enable Browser Based Authentication source.""",
    )
    browser_based_authentication_settings: BrowserBasedAuthSettingsEdit = Field(
        alias="browser-based-authentication-settings",
        description="""Browser Based Authentication settings.""",
    )
    identity_agent: bool = Field(
        alias="identity-agent", description="""Enable Identity Agent source."""
    )
    identity_agent_settings: IdentityAgentSettingsEdit = Field(
        alias="identity-agent-settings", description="""Identity Agent settings."""
    )
    identity_based_enforcement: str = Field(
        alias="identity-based-enforcement",
        description="""ON: Configures this object as a PEP-only object - identity-based enforcement (PEP) is enabled.<br>OFF: Configures this object as a PDP-only object - identity-based enforcement is disabled.""",
    )
    identity_collector: bool = Field(
        alias="identity-collector", description="""Enable Identity Collector source."""
    )
    identity_collector_settings: IdentityCollectorSettingsEdit = Field(
        alias="identity-collector-settings",
        description="""Identity Collector settings.""",
    )
    identity_sharing_settings: IdentitySharingSettingsEdit = Field(
        alias="identity-sharing-settings", description="""Identity sharing settings."""
    )
    identity_web_api: bool = Field(
        alias="identity-web-api", description="""Enable Identity Web API source."""
    )
    identity_web_api_settings: IdentityWebApiSettingsEdit = Field(
        alias="identity-web-api-settings", description="""Identity Web API settings."""
    )
    proxy_settings: IdaProxySettingsEdit = Field(
        alias="proxy-settings", description="""Identity-Awareness Proxy settings."""
    )
    remote_access: bool = Field(
        alias="remote-access", description="""Enable Remote Access Identity source."""
    )
