from advanced_properties_reply import AdvancedPropertiesReply
from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from encrypted_traffic_reply import EncryptedTrafficReply
from ike_p1_reply import IkeP1Reply
from ike_p2_reply import IkeP2Reply
from meshed_permanent_tunnels_reply import MeshedPermanentTunnelsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field
from route_based_settings_reply import RouteBasedSettingsReply
from wire_mode_reply import WireModeReply


class VpnMeshedCommunityReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    disable_nat: bool = Field(
        alias="disable-nat",
        description="""Indicates whether to disable NAT inside the VPN Community.""",
    )
    encrypted_traffic: EncryptedTrafficReply = Field(
        alias="encrypted-traffic", description="""Encrypted traffic settings."""
    )
    encryption_method: str = Field(
        alias="encryption-method", description="""The encryption method to be used."""
    )
    encryption_suite: str = Field(
        alias="encryption-suite", description="""The encryption suite to be used."""
    )
    excluded_services: list[dict] = Field(
        alias="excluded-services",
        description="""Collection of services that are excluded from the community identified by the name or UID.<br> Connections with these services will not be encrypted and will not match rules specifying the community in the VPN community. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    gateways: list[dict] = Field(
        alias="gateways",
        description="""Collection of VPN Gateway and VPN Device objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    granular_encryptions: list[dict] = Field(
        alias="granular-encryptions", description="""VPN granular encryption settings."""
    )
    ike_phase_1: IkeP1Reply = Field(
        alias="ike-phase-1",
        description="""Ike Phase 1 settings. Only applicable when the encryption-suite is set to [custom].""",
    )
    ike_phase_2: IkeP2Reply = Field(
        alias="ike-phase-2",
        description="""Ike Phase 2 settings. Only applicable when the encryption-suite is set to [custom].""",
    )
    link_selection_mode: str = Field(
        alias="link-selection-mode", description="""Link Selection Mode."""
    )
    override_interfaces: list[dict] = Field(
        alias="override-interfaces",
        description="""Override the Enhanced Link Selection interfaces for each participant VPN peer.""",
    )
    override_vpn_domains: list[dict] = Field(
        alias="override-vpn-domains",
        description="""The Overrides VPN Domains of the participants GWs.""",
    )
    permanent_tunnels: MeshedPermanentTunnelsReply = Field(
        alias="permanent-tunnels", description="""Permanent tunnels properties."""
    )
    shared_secrets: list[dict] = Field(
        alias="shared-secrets", description="""Shared secrets for external gateways."""
    )
    tunnel_granularity: str = Field(
        alias="tunnel-granularity", description="""VPN tunnel sharing option to be used."""
    )
    use_shared_secret: bool = Field(
        alias="use-shared-secret",
        description="""Indicates whether the shared secret should be used for all external gateways.""",
    )
    wire_mode: WireModeReply = Field(
        alias="wire-mode", description="""VPN Community Wire mode properties."""
    )
    routing_mode: str = Field(alias="routing-mode", description="""VPN Community Routing Mode.""")
    route_based_settings: RouteBasedSettingsReply = Field(
        alias="route-based-settings",
        description="""<html>VPN Community Route-Based settings.<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
    advanced_properties: AdvancedPropertiesReply = Field(
        alias="advanced-properties", description="""Advanced properties."""
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain", description="""Information about the domain that holds the Object."""
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
        alias="available-actions", description="""Actions that are available on the object."""
    )
