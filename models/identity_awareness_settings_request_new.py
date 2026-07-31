from browser_based_auth_settings_new import BrowserBasedAuthSettingsNew
from ida_proxy_settings_new import IdaProxySettingsNew
from identity_agent_settings_new import IdentityAgentSettingsNew
from identity_collector_settings_new import IdentityCollectorSettingsNew
from identity_sharing_settings_new import IdentitySharingSettingsNew
from pydantic import BaseModel, Field


class IdentityAwarenessSettingsRequestNew(BaseModel):
    browser_based_authentication: bool = Field(
        alias="browser-based-authentication",
        description="""Enable Browser Based Authentication source.""",
    )
    browser_based_authentication_settings: BrowserBasedAuthSettingsNew = Field(
        alias="browser-based-authentication-settings",
        description="""Browser Based Authentication settings.""",
    )
    identity_agent: bool = Field(
        alias="identity-agent", description="""Enable Identity Agent source."""
    )
    identity_agent_settings: IdentityAgentSettingsNew = Field(
        alias="identity-agent-settings", description="""Identity Agent settings."""
    )
    identity_based_enforcement: str = Field(
        alias="identity-based-enforcement",
        description="""ON: Configures this object as a PEP-only object - identity-based enforcement (PEP) is enabled.<br>OFF: Configures this object as a PDP-only object - identity-based enforcement is disabled.""",
    )
    identity_collector: bool = Field(
        alias="identity-collector", description="""Enable Identity Collector source."""
    )
    identity_collector_settings: IdentityCollectorSettingsNew = Field(
        alias="identity-collector-settings",
        description="""Identity Collector settings.""",
    )
    identity_sharing_settings: IdentitySharingSettingsNew = Field(
        alias="identity-sharing-settings", description="""Identity sharing settings."""
    )
    proxy_settings: IdaProxySettingsNew = Field(
        alias="proxy-settings", description="""Identity-Awareness Proxy settings."""
    )
    remote_access: bool = Field(
        alias="remote-access", description="""Enable Remote Access Identity source."""
    )
