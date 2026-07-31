from direct_tcp_settings_reply import DirectTcpSettingsReply
from pydantic import BaseModel, Field


class Cmpv1SettingsReply(BaseModel):
    direct_tcp_settings: DirectTcpSettingsReply = Field(
        alias="direct-tcp-settings",
        description="""Direct tcp transport layer settings.""",
    )
