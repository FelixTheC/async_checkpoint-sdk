from .direct_tcp_settings_reply import DirectTcpSettingsReply
from .https_settings_reply import HttpsSettingsReply
from .pydantic import BaseModel, Field


class Cmpv2SettingsReply(BaseModel):
    transport_layer: str = Field(alias="transport-layer", description="""Transport layer.""")
    direct_tcp_settings: DirectTcpSettingsReply = Field(
        alias="direct-tcp-settings",
        description="""Direct tcp transport layer settings.""",
    )
    http_settings: HttpsSettingsReply = Field(
        alias="http-settings", description="""Http transport layer settings."""
    )
