from direct_tcp_settings_request import DirectTcpSettingsRequest
from pydantic import BaseModel, Field


class Cmpv1SettingsRequest(BaseModel):
    direct_tcp_settings: DirectTcpSettingsRequest = Field(
        alias="direct-tcp-settings", description="""Direct tcp transport layer settings."""
    )
