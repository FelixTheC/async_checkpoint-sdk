from anti_spoofing_settings_reply import AntiSpoofingSettingsReply
from internal_topology_settings_reply import InternalTopologySettingsReply
from pydantic import BaseModel, Field
from security_zone_settings_reply import SecurityZoneSettingsReply


class NetworkInterfaceReply(BaseModel):
    ipv4_address: str = Field(alias="ipv4-address", description="""IPv4 address.""")
    ipv4_mask_length: int = Field(
        alias="ipv4-mask-length", description="""IPv4 network mask length."""
    )
    ipv4_network_mask: str = Field(
        alias="ipv4-network-mask", description="""IPv4 network mask."""
    )
    name: str = Field(alias="name", description="""Interface name.""")
    ipv6_address: str = Field(alias="ipv6-address", description="""IPv6 address.""")
    ipv6_mask_length: int = Field(
        alias="ipv6-mask-length", description="""IPv6 network mask length."""
    )
    ipv6_network_mask: str = Field(
        alias="ipv6-network-mask", description="""IPv6 network mask."""
    )
    anti_spoofing: bool = Field(alias="anti-spoofing", description="""N/A""")
    anti_spoofing_settings: AntiSpoofingSettingsReply = Field(
        alias="anti-spoofing-settings", description="""N/A"""
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    dynamic_ip: bool = Field(
        alias="dynamic-ip", description="""Enable dynamic interface."""
    )
    icon: str = Field(alias="icon", description="""Object icon.""")
    network_interface_type: str = Field(
        alias="network-interface-type", description="""Type of network interface."""
    )
    security_zone: bool = Field(alias="security-zone", description="""N/A""")
    security_zone_settings: SecurityZoneSettingsReply = Field(
        alias="security-zone-settings", description="""N/A"""
    )
    topology: str = Field(alias="topology", description="""Topology configuration.""")
    topology_automatic_calculation: str = Field(
        alias="topology-automatic-calculation",
        description="""Shows the automatic topology calculation.""",
    )
    topology_settings: InternalTopologySettingsReply = Field(
        alias="topology-settings", description="""Internal topology settings."""
    )
    uid: str = Field(alias="uid", description="""Network interface object UID.""")
