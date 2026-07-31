from pydantic import BaseModel, Field


class InternalTopologySettingsReply(BaseModel):
    interface_leads_to_dmz: bool = Field(
        alias="interface-leads-to-dmz",
        description="""Whether this interface leads to demilitarized zone (perimeter network).""",
    )
    ip_address_behind_this_interface: str = Field(
        alias="ip-address-behind-this-interface",
        description="""Network settings behind this interface.""",
    )
    specific_network: str = Field(
        alias="specific-network", description="""Network behind this interface."""
    )
    specific_network_uid: str = Field(
        alias="specific-network-uid", description="""N/A"""
    )
