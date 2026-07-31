from cluster_profile_anti_spoofing_settings_reply import (
    ClusterProfileAntiSpoofingSettingsReply,
)
from pydantic import BaseModel, Field


class ClusterProfileTopologyReply(BaseModel):
    anti_spoofing: bool = Field(alias="anti-spoofing", description="""N/A""")
    anti_spoofing_settings: ClusterProfileAntiSpoofingSettingsReply = Field(
        alias="anti-spoofing-settings", description="""N/A"""
    )
    interface_leads_to_dmz: bool = Field(
        alias="interface-leads-to-dmz", description="""N/A"""
    )
    ip_addresses_behind_this_interface: str = Field(
        alias="ip-addresses-behind-this-interface", description="""N/A"""
    )
    type: str = Field(alias="type", description="""N/A""")
