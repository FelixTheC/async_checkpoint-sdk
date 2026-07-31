from .anti_spoofing_settings_request import AntiSpoofingSettingsRequest
from .internal_topology_settings_request import InternalTopologySettingsRequest
from .object import Object
from .pydantic import BaseModel, Field
from .security_zone_settings_request import SecurityZoneSettingsRequest


class InterfaceRequestEdit(BaseModel):
    anti_spoofing: bool = Field(alias="anti-spoofing", description="""Enable anti-spoofing.""")
    anti_spoofing_settings: AntiSpoofingSettingsRequest = Field(
        alias="anti-spoofing-settings", description="""Anti Spoofing Settings."""
    )
    cluster_members: list[dict] = Field(
        alias="cluster-members",
        description="""Network interface settings for cluster members.""",
    )
    cluster_network_type: str = Field(
        alias="cluster-network-type", description="""Cluster interface type."""
    )
    dynamic_ip: bool = Field(alias="dynamic-ip", description="""Enable dynamic interface.""")
    ipv4_address: str = Field(alias="ipv4-address", description="""IPv4 network address.""")
    ipv4_mask_length: int = Field(alias="ipv4-mask-length", description="""IPv4 mask length.""")
    ipv4_network_mask: str = Field(alias="ipv4-network-mask", description="""IPv4 network mask.""")
    ipv6_address: str = Field(alias="ipv6-address", description="""IPv6 address.""")
    ipv6_mask_length: int = Field(alias="ipv6-mask-length", description="""IPv6 mask length.""")
    ipv6_network_mask: str = Field(alias="ipv6-network-mask", description="""IPv6 network mask.""")
    monitored_by_cluster: bool = Field(
        alias="monitored-by-cluster",
        description="""When Private is selected as the Cluster interface type, cluster can monitor or not monitor the interface.""",
    )
    network_interface_type: str = Field(
        alias="network-interface-type", description="""Network Interface Type."""
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    security_zone_settings: SecurityZoneSettingsRequest = Field(
        alias="security-zone-settings", description="""Security Zone Settings."""
    )
    topology: str = Field(alias="topology", description="""Topology configuration.""")
    topology_settings: InternalTopologySettingsRequest = Field(
        alias="topology-settings", description="""Topology Settings."""
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from .the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
    )
    tags: Object = Field(alias="tags", description="""Collection of tag identifiers.""")
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
