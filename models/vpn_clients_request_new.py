from pydantic import BaseModel, Field


class VpnClientsRequestNew(BaseModel):
    enable_endpoint_security_vpn: bool = Field(
        alias="enable-endpoint-security-vpn",
        description="""Enable endpoint security vpn.""",
    )
    enable_cp_mobile_for_windows: bool = Field(
        alias="enable-cp-mobile-for-windows",
        description="""Enable Check Point Mobile for Windows client support.""",
    )
    enable_secu_remote: bool = Field(
        alias="enable-secu-remote", description="""Enable SecuRemote client support."""
    )
    enable_capsule_vpn_connect: bool = Field(
        alias="enable-capsule-vpn-connect",
        description="""Enable Capsule VPN Connect client support.""",
    )
    enable_ssl_network_extender: bool = Field(
        alias="enable-ssl-network-extender",
        description="""Enable SSL Network Extender client support.""",
    )
    gateway_authentication_certificate: str = Field(
        alias="gateway-authentication-certificate",
        description="""The certificate used for gateway authentication, identified by name or UID.""",
    )
