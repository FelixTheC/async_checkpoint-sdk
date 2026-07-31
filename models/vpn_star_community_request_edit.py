from add import add
from advanced_properties_request import AdvancedPropertiesRequest
from enhanced_link_selection_interfaces_per_participant_request_add_and_edit import (
    EnhancedLinkSelectionInterfacesPerParticipantRequestAddAndEdit,
)
from granular_encryption_request import GranularEncryptionRequest
from ike_p1_request import IkeP1Request
from ike_p2_request import IkeP2Request
from multiple_entry_points_request_edit import MultipleEntryPointsRequestEdit
from participants_domains_request import ParticipantsDomainsRequest
from pydantic import BaseModel, Field
from remove import remove
from route_based_settings_request_edit import RouteBasedSettingsRequestEdit
from shared_secret_request import SharedSecretRequest
from star_encrypted_traffic_request import StarEncryptedTrafficRequest
from star_permanent_tunnels_request_edit import StarPermanentTunnelsRequestEdit
from wire_mode_request import WireModeRequest


class VpnStarCommunityRequestEdit(BaseModel):
    center_gateways: add | remove | str | list[str] = Field(
        alias="center-gateways",
        description="""Collection of center VPN Gateway and VPN Device objects identified by the name or UID.""",
    )
    disable_nat: bool = Field(
        alias="disable-nat",
        description="""Indicates whether to disable NAT inside the VPN Community.""",
    )
    disable_nat_on: str = Field(
        alias="disable-nat-on",
        description="""Indicates on which gateways to disable NAT inside the VPN Community.""",
    )
    encrypted_traffic: StarEncryptedTrafficRequest = Field(
        alias="encrypted-traffic", description="""Encrypted traffic settings."""
    )
    encryption_method: str = Field(
        alias="encryption-method", description="""The encryption method to be used."""
    )
    encryption_suite: str = Field(
        alias="encryption-suite", description="""The encryption suite to be used."""
    )
    excluded_services: add | remove | str | list[str] = Field(
        alias="excluded-services",
        description="""Collection of services that are excluded from the community identified by the name or UID.<br> Connections with these services will not be encrypted and will not match rules specifying the community in the VPN community.""",
    )
    granular_encryptions: add | remove | GranularEncryptionRequest | list[dict] = Field(
        alias="granular-encryptions",
        description="""VPN granular encryption settings.""",
    )
    ike_phase_1: IkeP1Request = Field(
        alias="ike-phase-1",
        description="""Ike Phase 1 settings. Only applicable when the encryption-suite is set to [custom].""",
    )
    ike_phase_2: IkeP2Request = Field(
        alias="ike-phase-2",
        description="""Ike Phase 2 settings. Only applicable when the encryption-suite is set to [custom].""",
    )
    link_selection_mode: str = Field(
        alias="link-selection-mode", description="""Link Selection Mode."""
    )
    mep: MultipleEntryPointsRequestEdit = Field(
        alias="mep", description="""Multiple Entry Point properties."""
    )
    mesh_center_gateways: bool = Field(
        alias="mesh-center-gateways",
        description="""Indicates whether the meshed community is in center.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    override_interfaces: (
        add
        | remove
        | EnhancedLinkSelectionInterfacesPerParticipantRequestAddAndEdit
        | list[dict]
    ) = Field(
        alias="override-interfaces",
        description="""Override the Enhanced Link Selection interfaces for each participant VPN peer.""",
    )
    override_vpn_domains: add | remove | ParticipantsDomainsRequest | list[dict] = (
        Field(
            alias="override-vpn-domains",
            description="""The Overrides VPN Domains of the participants GWs.""",
        )
    )
    permanent_tunnels: StarPermanentTunnelsRequestEdit = Field(
        alias="permanent-tunnels", description="""Permanent tunnels properties."""
    )
    satellite_gateways: add | remove | str | list[str] = Field(
        alias="satellite-gateways",
        description="""Collection of satellite VPN Gateway and VPN Device objects identified by the name or UID.""",
    )
    shared_secrets: add | remove | SharedSecretRequest | list[dict] = Field(
        alias="shared-secrets", description="""Shared secrets for external gateways."""
    )
    tunnel_granularity: str = Field(
        alias="tunnel-granularity",
        description="""VPN tunnel sharing option to be used.""",
    )
    use_shared_secret: bool = Field(
        alias="use-shared-secret",
        description="""Indicates whether the shared secret should be used for all external gateways.""",
    )
    vpn_routing: str = Field(
        alias="vpn-routing", description="""Enable VPN routing to satellites."""
    )
    wire_mode: WireModeRequest = Field(
        alias="wire-mode", description="""VPN Community Wire mode properties."""
    )
    routing_mode: str = Field(
        alias="routing-mode", description="""VPN Community Routing Mode."""
    )
    route_based_settings: RouteBasedSettingsRequestEdit = Field(
        alias="route-based-settings",
        description="""<html>VPN Community Route-Based settings.<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
    advanced_properties: AdvancedPropertiesRequest = Field(
        alias="advanced-properties", description="""Advanced properties."""
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    tags: add | remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
