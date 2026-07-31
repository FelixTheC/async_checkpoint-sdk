from pydantic import BaseModel, Field
from ssl_network_extender_reply import SslNetworkExtenderReply
from v_c_settings_for_gateway_reply import VCSettingsForGatewayReply


class VpnReply(BaseModel):
    is_third_party_encryption: bool = Field(
        alias="is-third-party-encryption",
        description="""Indicates if this device is an Interoperable Device.""",
    )
    isakmp_ipcomp_support: bool = Field(
        alias="isakmp-ipcomp-support",
        description="""Enables the ISAKMP IPCOMP (IP payload compression) between the Security Gateway and the Interoperable Device.""",
    )
    ssl_network_extender: SslNetworkExtenderReply = Field(
        alias="ssl-network-extender",
        description="""SSL Network Extender properties for the device.""",
    )
    vpn_clients_settings_for_gateway: VCSettingsForGatewayReply = Field(
        alias="vpn-clients-settings-for-gateway",
        description="""VPN client settings for the VPN Gateway.""",
    )
