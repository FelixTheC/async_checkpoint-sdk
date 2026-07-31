from .endpoint_connect_global_properties_request import (
    EndpointConnectGlobalPropertiesRequest,
)
from .hot_spot_hotel_registration_request import HotSpotHotelRegistrationRequest
from .pydantic import BaseModel, Field
from .scv_global_properties_request import ScvGlobalPropertiesRequest
from .secure_client_mobile_global_properties_request import (
    SecureClientMobileGlobalPropertiesRequest,
)
from .ssl_network_extender_global_properties_request import (
    SslNetworkExtenderGlobalPropertiesRequest,
)
from .vpn_advanced_global_properties_request import VpnAdvancedGlobalPropertiesRequest
from .vpn_auth_and_encryption_global_properties_request import (
    VpnAuthAndEncryptionGlobalPropertiesRequest,
)


class RemoteAccessGlobalPropertiesRequest(BaseModel):
    enable_back_connections: bool = Field(
        alias="enable-back-connections",
        description="""Usually communication with remote clients must be initialized by the clients. However, once a client has opened a connection, the hosts behind VPN can open a return or back connection to the client. For a back connection, the client's details must be maintained on all the devices between the client and the gateway, and on the gateway itself. Determine whether the back connection is enabled.""",
    )
    keep_alive_packet_to_gw_interval: int = Field(
        alias="keep-alive-packet-to-gw-interval",
        description="""Usually communication with remote clients must be initialized by the clients. However, once a client has opened a connection, the hosts behind VPN can open a return or back connection to the client. For a back connection, the client's details must be maintained on all the devices between the client and the gateway, and on the gateway itself. Determine frequency (in seconds) of the Keep Alive packets sent by the client in order to maintain the connection with the gateway.<br>Available only if enable-back-connections is true.""",
    )
    encrypt_dns_traffic: bool = Field(
        alias="encrypt-dns-traffic",
        description="""You can decide whether DNS queries sent by the remote client to a DNS server located on the corporate LAN are passed through the VPN tunnel or not. Disable this option if the client has to make DNS queries to the DNS server on the corporate LAN while connecting to the organization but without using the SecuRemote client.""",
    )
    simultaneous_login_mode: str = Field(
        alias="simultaneous-login-mode",
        description="""Select the simultaneous login mode.""",
    )
    vpn_authentication_and_encryption: VpnAuthAndEncryptionGlobalPropertiesRequest = Field(
        alias="vpn-authentication-and-encryption",
        description="""configure supported Encryption and Authentication methods for Remote Access clients.""",
    )
    vpn_advanced: VpnAdvancedGlobalPropertiesRequest = Field(
        alias="vpn-advanced",
        description="""Configure encryption methods and interface resolution for remote access clients.""",
    )
    scv: ScvGlobalPropertiesRequest = Field(
        alias="scv",
        description="""Define properties of the Secure Configuration Verification process.""",
    )
    ssl_network_extender: SslNetworkExtenderGlobalPropertiesRequest = Field(
        alias="ssl-network-extender",
        description="""Define properties for SSL Network Extender users.""",
    )
    secure_client_mobile: SecureClientMobileGlobalPropertiesRequest = Field(
        alias="secure-client-mobile",
        description="""Define properties for SecureClient Mobile.""",
    )
    endpoint_connect: EndpointConnectGlobalPropertiesRequest = Field(
        alias="endpoint-connect",
        description="""Configure global settings for Endpoint Connect. These settings apply to all gateways.""",
    )
    hot_spot_and_hotel_registration: HotSpotHotelRegistrationRequest = Field(
        alias="hot-spot-and-hotel-registration",
        description="""Configure the settings for Wireless Hot Spot and Hotel Internet access registration.""",
    )
