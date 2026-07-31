from anti_spoofing_settings_reply import AntiSpoofingSettingsReply
from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from gateway_description import GatewayDescription
from internal_topology_settings_reply import InternalTopologySettingsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field
from security_zone_settings_reply import SecurityZoneSettingsReply


class InterfaceReply(BaseModel):
    name: str = Field(alias="name", description="""Network interface name.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    gateway: GatewayDescription = Field(
        alias="gateway",
        description="""Properties of the gateway or cluster that the interface belongs to.""",
    )
    type: str = Field(alias="type", description="""Object type.""")
    anti_spoofing: bool = Field(
        alias="anti-spoofing", description="""Enable anti-spoofing."""
    )
    anti_spoofing_settings: AntiSpoofingSettingsReply = Field(
        alias="anti-spoofing-settings", description="""Anti Spoofing Settings."""
    )
    cluster_members: list[dict] = Field(
        alias="cluster-members",
        description="""Network interface settings for cluster members.""",
    )
    cluster_network_type: str = Field(
        alias="cluster-network-type", description="""Cluster interface type."""
    )
    dynamic_ip: bool = Field(
        alias="dynamic-ip", description="""Enable dynamic interface."""
    )
    ipv4_address: str = Field(
        alias="ipv4-address", description="""IPv4 network address."""
    )
    ipv4_mask_length: int = Field(
        alias="ipv4-mask-length", description="""IPv4 mask length."""
    )
    ipv4_network_mask: str = Field(
        alias="ipv4-network-mask", description="""IPv4 network mask."""
    )
    ipv6_address: str = Field(alias="ipv6-address", description="""IPv6 address.""")
    ipv6_mask_length: int = Field(
        alias="ipv6-mask-length", description="""IPv6 mask length."""
    )
    ipv6_network_mask: str = Field(
        alias="ipv6-network-mask", description="""IPv6 network mask."""
    )
    monitored_by_cluster: bool = Field(
        alias="monitored-by-cluster",
        description="""When Private is selected as the Cluster interface type, cluster can monitor or not monitor the interface.""",
    )
    network_interface_type: str = Field(
        alias="network-interface-type", description="""Network Interface Type."""
    )
    security_zone_settings: SecurityZoneSettingsReply = Field(
        alias="security-zone-settings", description="""Security Zone Settings."""
    )
    topology: str = Field(alias="topology", description="""Topology configuration.""")
    topology_automatic: str = Field(
        alias="topology-automatic",
        description="""Topology configuration automatically calculated by get-interfaces command.""",
    )
    topology_manual: str = Field(
        alias="topology-manual",
        description="""Topology configuration manually defined.""",
    )
    topology_settings: InternalTopologySettingsReply = Field(
        alias="topology-settings",
        description="""Automatic topology configuration when 'topology' set to automatic or manual if it is internal or external.""",
    )
    topology_settings_automatic: InternalTopologySettingsReply = Field(
        alias="topology-settings-automatic",
        description="""Topology settings automatically calculated by get-interfaces command.""",
    )
    topology_settings_manual: InternalTopologySettingsReply = Field(
        alias="topology-settings-manual",
        description="""Topology settings manually defined.""",
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    icon: str = Field(alias="icon", description="""Object icon.""")
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
    read_only: bool = Field(
        alias="read-only", description="""Indicates whether the object is read-only."""
    )
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
