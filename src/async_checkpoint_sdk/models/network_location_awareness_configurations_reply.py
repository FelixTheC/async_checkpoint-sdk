from api_object_standard_identifier import ApiObjectStandardIdentifier
from pydantic import BaseModel, Field


class NetworkLocationAwarenessConfigurationsReply(BaseModel):
    vpn_clients_are_considered_inside_the_internal_network_when_the_client: str = Field(
        alias="vpn-clients-are-considered-inside-the-internal-network-when-the-client",
        description="""When a VPN client is within the internal network, the internal resources are available and the VPN tunnel should be disconnected. Determine when VPN clients are considered inside the internal network:<br>Connects to GW through internal interface - The client connects to the gateway through one of its internal interfaces (recommended).<br>Connects from network or group - The client connects from a network or group specified in network-or-group-of-conn-vpn-client.<br>Runs on computer with access to Active Directory domain - The client runs on a computer that can access its Active Directory domain.<br>Note: The VPN tunnel will resume automatically when the VPN client is no longer in the internal network and the client is set to Always connected mode.""",
    )
    network_or_group_of_conn_vpn_client: ApiObjectStandardIdentifier = Field(
        alias="network-or-group-of-conn-vpn-client",
        description="""Name or UID of Network or Group the VPN client is connected from.<br>Available only if vpn-clients-are-considered-inside-the-internal-network-when-the-client is set to Connects from network or group.""",
    )
    consider_wireless_networks_as_external: bool = Field(
        alias="consider-wireless-networks-as-external",
        description="""The speed at which locations are classified as internal or external can be increased by creating a list of wireless networks that are known to be external. A wireless network is identified by its Service Set Identifier (SSID) a name used to identify a particular 802.11 wireless LAN.""",
    )
    dns_suffixes: list[str] = Field(
        alias="dns-suffixes",
        description="""DNS suffixes not defined here will be considered as external. If this list is empty consider-undefined-dns-suffixes-as-external will automatically be set to false.<br>Available only if consider-undefined-dns-suffixes-as-external is set to true.""",
    )
    excluded_internal_wireless_networks: list[str] = Field(
        alias="excluded-internal-wireless-networks",
        description="""Excludes the specified internal networks names (SSIDs).<br>Available only if consider-wireless-networks-as-external is set to true.""",
    )
    consider_undefined_dns_suffixes_as_external: bool = Field(
        alias="consider-undefined-dns-suffixes-as-external",
        description="""The speed at which locations are classified as internal or external can be increased by creating a list of DNS suffixes that are known to be external. Enable this to be able to define DNS suffixes which won't be considered external.""",
    )
    remember_previously_detected_external_networks: bool = Field(
        alias="remember-previously-detected-external-networks",
        description="""The speed at which locations are classified as internal or external can be increased by caching (on the client side) names of networks that were previously determined to be external.""",
    )
