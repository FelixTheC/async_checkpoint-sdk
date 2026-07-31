from pydantic import BaseModel, Field


class SecureClientMobileGlobalPropertiesRequest(BaseModel):
    user_auth_method: str = Field(
        alias="user-auth-method",
        description="""Wide Impact: Also applies for SSL Network Extender clients and Check Point GO clients.<br>How the user will be authenticated by the gateway.""",
    )
    enable_password_caching: str = Field(
        alias="enable-password-caching",
        description="""If the password entered to authenticate is saved locally on the user's machine.""",
    )
    cache_password_timeout: int = Field(
        alias="cache-password-timeout",
        description="""Cached password timeout (in minutes).""",
    )
    re_auth_user_interval: int = Field(
        alias="re-auth-user-interval",
        description="""Wide Impact: Also applies for SSL Network Extender clients!<br>The length of time (in minutes) until the user's credentials are resent to the gateway to verify authorization.""",
    )
    connect_mode: str = Field(
        alias="connect-mode",
        description="""Methods by which a connection to the gateway will be initiated:<br>Configured On Endpoint Client - the method used for initiating a connection to a gateway is determined by the endpoint client<br>Manual - VPN connections will not be initiated automatically.<br>Always connected - SecureClient Mobile will automatically establish a connection to the last connected gateway under the following circumstances: (a) the device has a valid IP address, (b) when the device wakes up from a low-power state or a soft-reset, or (c) after a condition that caused the device to automatically disconnect ceases to exist (for example, Device is out of PC Sync, Disconnect is not idle.).<br>On application request - Applications requiring access to resources through the VPN will be able to initiate a VPN connection.""",
    )
    automatically_initiate_dialup: str = Field(
        alias="automatically-initiate-dialup",
        description="""When selected, the client will initiate a GPRS dialup connection before attempting to establish the VPN connection. Note that if a local IP address is already available through another network interface, then the GPRS dialup is not initiated.""",
    )
    disconnect_when_device_is_idle: str = Field(
        alias="disconnect-when-device-is-idle",
        description="""Enabling this feature will disconnect users from the gateway if there is no traffic sent during the defined time period.""",
    )
    supported_encryption_methods: str = Field(
        alias="supported-encryption-methods",
        description="""Wide Impact: Also applies for SSL Network Extender clients!<br>Select the encryption algorithms that will be supported with remote users.""",
    )
    route_all_traffic_to_gw: str = Field(
        alias="route-all-traffic-to-gw",
        description="""Operates the client in Hub Mode, sending all traffic to the VPN server for routing, filtering, and processing.""",
    )
