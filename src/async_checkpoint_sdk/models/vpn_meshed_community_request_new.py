from advanced_properties_request import AdvancedPropertiesRequest
from encrypted_traffic_request_new import EncryptedTrafficRequestNew
from enhanced_link_selection_interfaces_per_participant_request_add_and_edit import (
    EnhancedLinkSelectionInterfacesPerParticipantRequestAddAndEdit,
)
from granular_encryption_request import GranularEncryptionRequest
from ike_p1_request_new import IkeP1RequestNew
from ike_p2_request_new import IkeP2RequestNew
from meshed_permanent_tunnels_request_new import MeshedPermanentTunnelsRequestNew
from participants_domains_request import ParticipantsDomainsRequest
from pydantic import BaseModel, Field
from route_based_settings_request_new import RouteBasedSettingsRequestNew
from shared_secret_request import SharedSecretRequest
from wire_mode_request import WireModeRequest


class VpnMeshedCommunityRequestNew(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    disable_nat: bool = Field(
        alias="disable-nat",
        description="""Indicates whether to disable NAT inside the VPN Community.""",
    )
    encrypted_traffic: EncryptedTrafficRequestNew = Field(
        alias="encrypted-traffic", description="""Encrypted traffic settings."""
    )
    encryption_method: str = Field(
        alias="encryption-method", description="""The encryption method to be used."""
    )
    encryption_suite: str = Field(
        alias="encryption-suite", description="""The encryption suite to be used."""
    )
    excluded_services: str | list[str] = Field(
        alias="excluded-services",
        description="""Collection of services that are excluded from the community identified by the name or UID.<br> Connections with these services will not be encrypted and will not match rules specifying the community in the VPN community.""",
    )
    gateways: str | list[str] = Field(
        alias="gateways",
        description="""Collection of VPN Gateway and VPN Device objects identified by the name or UID.""",
    )
    granular_encryptions: GranularEncryptionRequest | list[dict] = Field(
        alias="granular-encryptions", description="""VPN granular encryption settings."""
    )
    ike_phase_1: IkeP1RequestNew = Field(
        alias="ike-phase-1",
        description="""Ike Phase 1 settings. Only applicable when the encryption-suite is set to [custom].""",
    )
    ike_phase_2: IkeP2RequestNew = Field(
        alias="ike-phase-2",
        description="""Ike Phase 2 settings. Only applicable when the encryption-suite is set to [custom].""",
    )
    link_selection_mode: str = Field(
        alias="link-selection-mode", description="""Link Selection Mode."""
    )
    override_interfaces: (
        EnhancedLinkSelectionInterfacesPerParticipantRequestAddAndEdit | list[dict]
    ) = Field(
        alias="override-interfaces",
        description="""Override the Enhanced Link Selection interfaces for each participant VPN peer.""",
    )
    override_vpn_domains: ParticipantsDomainsRequest | list[dict] = Field(
        alias="override-vpn-domains",
        description="""The Overrides VPN Domains of the participants GWs.""",
    )
    permanent_tunnels: MeshedPermanentTunnelsRequestNew = Field(
        alias="permanent-tunnels", description="""Permanent tunnels properties."""
    )
    shared_secrets: SharedSecretRequest | list[dict] = Field(
        alias="shared-secrets", description="""Shared secrets for external gateways."""
    )
    tunnel_granularity: str = Field(
        alias="tunnel-granularity", description="""VPN tunnel sharing option to be used."""
    )
    use_shared_secret: bool = Field(
        alias="use-shared-secret",
        description="""Indicates whether the shared secret should be used for all external gateways.""",
    )
    wire_mode: WireModeRequest = Field(
        alias="wire-mode", description="""VPN Community Wire mode properties."""
    )
    routing_mode: str = Field(alias="routing-mode", description="""VPN Community Routing Mode.""")
    route_based_settings: RouteBasedSettingsRequestNew = Field(
        alias="route-based-settings",
        description="""<html>VPN Community Route-Based settings.<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
    advanced_properties: AdvancedPropertiesRequest = Field(
        alias="advanced-properties", description="""Advanced properties."""
    )
    set_if_exists: bool = Field(
        alias="set-if-exists",
        description="""If another object with the same identifier already exists, it will be updated. The command behaviour will be the same as if originally a set command was called. Pay attention that original object's fields will be overwritten by the fields provided in the request payload!""",
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
