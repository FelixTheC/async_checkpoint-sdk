from .browser_based_auth_settings_reply import BrowserBasedAuthSettingsReply
from .ida_proxy_settings_reply import IdaProxySettingsReply
from .identity_agent_settings_reply import IdentityAgentSettingsReply
from .identity_collector_settings_reply import IdentityCollectorSettingsReply
from .identity_sharing_settings_reply import IdentitySharingSettingsReply
from .identity_web_api_settings_reply import IdentityWebApiSettingsReply
from .pydantic import BaseModel, Field


class IdentityAwarenessSettingsReply(BaseModel):
    ad_query: bool = Field(alias="ad-query", description="""AD Query source enabled.""")
    browser_based_authentication: bool = Field(
        alias="browser-based-authentication",
        description="""Browser Based Authentication source enabled.""",
    )
    browser_based_authentication_settings: BrowserBasedAuthSettingsReply = Field(
        alias="browser-based-authentication-settings",
        description="""Browser Based Authentication settings.""",
    )
    collecting_identities: bool = Field(
        alias="collecting-identities",
        description="""This gateway collects identities.""",
    )
    identity_agent: bool = Field(
        alias="identity-agent", description="""Identity Agent source enabled."""
    )
    identity_agent_settings: IdentityAgentSettingsReply = Field(
        alias="identity-agent-settings", description="""Identity Agent settings."""
    )
    identity_based_enforcement: str = Field(
        alias="identity-based-enforcement",
        description="""ON: Configures this object as a PEP-only object - identity-based enforcement (PEP) is enabled.<br>OFF: Configures this object as a PDP-only object - identity-based enforcement is disabled.""",
    )
    identity_collector: bool = Field(
        alias="identity-collector", description="""Identity Collector source enabled."""
    )
    identity_collector_settings: IdentityCollectorSettingsReply = Field(
        alias="identity-collector-settings",
        description="""Identity Collector settings.""",
    )
    identity_sharing_settings: IdentitySharingSettingsReply = Field(
        alias="identity-sharing-settings", description="""Identity sharing settings."""
    )
    identity_web_api: bool = Field(
        alias="identity-web-api", description="""Identity Web API source enabled."""
    )
    identity_web_api_settings: IdentityWebApiSettingsReply = Field(
        alias="identity-web-api-settings", description="""Identity Web API settings."""
    )
    proxy_settings: IdaProxySettingsReply = Field(
        alias="proxy-settings", description="""Identity-Awareness Proxy settings."""
    )
    radius_accounting: bool = Field(
        alias="radius-accounting", description="""Radius Accounting source enabled."""
    )
    remote_access: bool = Field(
        alias="remote-access", description="""Remote Access source enabled."""
    )
    terminal_servers: bool = Field(
        alias="terminal-servers", description="""Terminal Servers source enabled."""
    )
