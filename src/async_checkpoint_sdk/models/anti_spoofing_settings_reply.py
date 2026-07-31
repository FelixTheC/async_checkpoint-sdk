from .pydantic import BaseModel, Field


class AntiSpoofingSettingsReply(BaseModel):
    action: str = Field(
        alias="action",
        description="""If packets will be rejected (the Prevent option) or whether the packets will be monitored (the Detect option).""",
    )
    exclude_packets: bool = Field(
        alias="exclude-packets",
        description="""Don't check packets from .excluded network.""",
    )
    excluded_network_name: str = Field(
        alias="excluded-network-name", description="""Excluded network name."""
    )
    excluded_network_uid: str = Field(
        alias="excluded-network-uid", description="""Excluded network UID."""
    )
    spoof_tracking: str = Field(alias="spoof-tracking", description="""Spoof tracking.""")
