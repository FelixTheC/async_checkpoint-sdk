from direct_tcp_settings_request import DirectTcpSettingsRequest
from https_settings_request import HttpsSettingsRequest
from pydantic import BaseModel, Field


class Cmpv2SettingsRequest(BaseModel):
    transport_layer: str = Field(
        alias="transport-layer", description="""Transport layer."""
    )
    direct_tcp_settings: DirectTcpSettingsRequest = Field(
        alias="direct-tcp-settings",
        description="""Direct tcp transport layer settings.""",
    )
    http_settings: HttpsSettingsRequest = Field(
        alias="http-settings", description="""Http transport layer settings."""
    )
