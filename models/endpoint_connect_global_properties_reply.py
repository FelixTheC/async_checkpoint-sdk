from network_location_awareness_configurations_reply import (
    NetworkLocationAwarenessConfigurationsReply,
)
from pydantic import BaseModel, Field


class EndpointConnectGlobalPropertiesReply(BaseModel):
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
        description="""The length of time (in minutes) until the user's credentials are resent to the gateway to verify authorization.""",
    )
    connect_mode: str = Field(
        alias="connect-mode",
        description="""Methods by which a connection to the gateway will be initiated:<br>Manual - VPN connections will not be initiated automatically.<br>Always connected - Endpoint Connect will automatically establish a connection to the last connected gateway under the following circumstances: (a) the device has a valid IP address, (b) when the device wakes up from a low-power state or a soft-reset, or (c) after a condition that caused the device to automatically disconnect ceases to exist (for example, Device is out of PC Sync, Disconnect is not idle.).<br>Configured on endpoint client - the method used for initiating a connection to a gateway is determined by the endpoint client.""",
    )
    network_location_awareness: str = Field(
        alias="network-location-awareness",
        description="""Wide Impact: Also applies for Check Point GO clients!<br>Endpoint Connect intelligently detects whether it is inside or outside of the VPN domain (Enterprise LAN), and automatically connects or disconnects as required. Select true and edit network-location-awareness-conf to configure this capability.""",
    )
    network_location_awareness_conf: NetworkLocationAwarenessConfigurationsReply = Field(
        alias="network-location-awareness-conf",
        description="""Configure how the client determines its location in relation to the internal network.""",
    )
    disconnect_when_conn_to_network_is_lost: str = Field(
        alias="disconnect-when-conn-to-network-is-lost",
        description="""Enabling this feature disconnects users from the gateway when connectivity to the network is lost.""",
    )
    disconnect_when_device_is_idle: str = Field(
        alias="disconnect-when-device-is-idle",
        description="""Enabling this feature will disconnect users from the gateway if there is no traffic sent during the defined time period.""",
    )
    route_all_traffic_to_gw: str = Field(
        alias="route-all-traffic-to-gw",
        description="""Operates the client in Hub Mode, sending all traffic to the VPN server for routing, filtering, and processing.""",
    )
    client_upgrade_mode: str = Field(
        alias="client-upgrade-mode",
        description="""Select an option to determine how the client is upgraded.""",
    )
