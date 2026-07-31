from pydantic import BaseModel, Field


class ClusterProfileAntiSpoofingSettingsReply(BaseModel):
    action: str = Field(alias="action", description="""N/A""")
    do_not_check_specific_packets: bool = Field(
        alias="do-not-check-specific-packets", description="""N/A"""
    )
    do_not_check_specific_packets_from: str = Field(
        alias="do-not-check-specific-packets-from", description="""N/A"""
    )
    spoof_tracking: str = Field(alias="spoof-tracking", description="""N/A""")
