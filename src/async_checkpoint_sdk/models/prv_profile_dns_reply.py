from .pydantic import BaseModel, Field


class PrvProfileDnsReply(BaseModel):
    manage_settings: str = Field(
        alias="manage-settings",
        description="""Manage settings mode: locally on the device or centrally from .this application.""",
    )
    override_settings: str = Field(
        alias="override-settings",
        description="""Override settings mode: allowed, mandatory or denied. Relevant only when settings are managed centrally.""",
    )
    dns_proxy: bool = Field(alias="dns-proxy", description="""DNS proxy enabled.""")
    primary_server: str = Field(alias="primary-server", description="""Primary DNS Server.""")
    secondary_server: str = Field(alias="secondary-server", description="""Secondary DNS Server.""")
    servers_configuration_mode: str = Field(
        alias="servers-configuration-mode",
        description="""Servers configuration mode.
Auto- dns configuration provided by the active internet connection.
Manual- set dns servers configuration manually.""",
    )
    tertiary_server: str = Field(alias="tertiary-server", description="""Tertiary DNS Server.""")
