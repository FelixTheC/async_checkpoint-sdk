from .api_object_standard_identifier import ApiObjectStandardIdentifier
from .pydantic import BaseModel, Field


class GatewayServerInterfaceTopologyReply(BaseModel):
    leads_to_internet: bool = Field(
        alias="leads-to-internet",
        description="""Gets true if the interface is external.""",
    )
    ip_address_behind_this_interface: str = Field(
        alias="ip-address-behind-this-interface",
        description="""If the interface is internal, this field specifies to which network it leads.""",
    )
    leads_to_specific_network: ApiObjectStandardIdentifier = Field(
        alias="leads-to-specific-network",
        description="""If ip-address-behind-this-interface is set to 'Specific', this field shows information about the network object hidden behind this interface. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    leads_to_dmz: bool = Field(
        alias="leads-to-dmz", description="""Gets true if the interface leads to DMZ."""
    )
    security_zone: ApiObjectStandardIdentifier = Field(
        alias="security-zone",
        description="""This field shows Security Zone object. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
