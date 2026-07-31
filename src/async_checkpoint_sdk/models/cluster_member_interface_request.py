from anti_spoofing_settings_request import AntiSpoofingSettingsRequest
from internal_topology_settings_request import InternalTopologySettingsRequest
from object import Object
from pydantic import BaseModel, Field
from security_zone_settings_request import SecurityZoneSettingsRequest


class ClusterMemberInterfaceRequest(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    anti_spoofing: bool = Field(alias="anti-spoofing", description="""N/A""")
    anti_spoofing_settings: AntiSpoofingSettingsRequest = Field(
        alias="anti-spoofing-settings", description="""N/A"""
    )
    dynamic_ip: bool = Field(
        alias="dynamic-ip",
        description="""The Topology of interface with Dynamic IP is set to Automatic - External.""",
    )
    ip_address: str = Field(
        alias="ip-address",
        description="""IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly.""",
    )
    network_mask: str = Field(
        alias="network-mask",
        description="""IPv4 or IPv6 network mask. If both masks are required use ipv4-network-mask and ipv6-network-mask fields explicitly. Instead of providing mask itself it is possible to specify IPv4 or IPv6 mask length in mask-length field. If both masks length are required use ipv4-mask-length and  ipv6-mask-length fields explicitly.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    security_zone: bool = Field(alias="security-zone", description="""N/A""")
    security_zone_settings: SecurityZoneSettingsRequest = Field(
        alias="security-zone-settings", description="""N/A"""
    )
    topology: str = Field(alias="topology", description="""N/A""")
    topology_settings: InternalTopologySettingsRequest = Field(
        alias="topology-settings", description="""N/A"""
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    tags: Object = Field(alias="tags", description="""Collection of tag identifiers.""")
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
