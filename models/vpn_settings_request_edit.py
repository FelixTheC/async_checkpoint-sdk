from add import add
from authentication_request_edit import AuthenticationRequestEdit
from clientless_vpn_settings_request_edit import ClientlessVpnSettingsRequestEdit
from complete import complete
from enhanced_link_selection_interfaces_request import (
    EnhancedLinkSelectionInterfacesRequest,
)
from exported_routes_request_edit import ExportedRoutesRequestEdit
from link_selection_request_edit import LinkSelectionRequestEdit
from office_mode_request import OfficeModeRequest
from pydantic import BaseModel, Field
from remote_access_request import RemoteAccessRequest
from remove import remove
from renew import renew
from saml_portal_request_edit import SamlPortalRequestEdit
from vpn_advanced_request_edit import VpnAdvancedRequestEdit
from vpn_clients_request_edit import VpnClientsRequestEdit


class VpnSettingsRequestEdit(BaseModel):
    advanced: VpnAdvancedRequestEdit = Field(
        alias="advanced", description="""Advanced VPN settings."""
    )
    authentication: AuthenticationRequestEdit = Field(
        alias="authentication", description="""Authentication."""
    )
    certificates: add | renew | complete | remove = Field(
        alias="certificates", description="""Vpn certificates."""
    )
    exported_routes: ExportedRoutesRequestEdit = Field(
        alias="exported-routes",
        description="""<html>Exported Routes.<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
    interfaces: add | remove | EnhancedLinkSelectionInterfacesRequest | list[dict] = (
        Field(alias="interfaces", description="""Enhanced Link Selection Interfaces.""")
    )
    link_selection: LinkSelectionRequestEdit = Field(
        alias="link-selection", description="""Link Selection."""
    )
    maximum_concurrent_ike_negotiations: int = Field(
        alias="maximum-concurrent-ike-negotiations", description="""N/A"""
    )
    maximum_concurrent_tunnels: int = Field(
        alias="maximum-concurrent-tunnels", description="""N/A"""
    )
    office_mode: OfficeModeRequest = Field(
        alias="office-mode",
        description="""Office Mode.
Notation Wide Impact - Office Mode apply IPSec VPN Software Blade clients and to the Mobile Access Software Blade clients.""",
    )
    remote_access: RemoteAccessRequest = Field(
        alias="remote-access", description="""Remote Access."""
    )
    saml_portal_settings: SamlPortalRequestEdit = Field(
        alias="saml-portal-settings",
        description="""Configuration of the SAML portal for VPN authentication.""",
    )
    vpn_clients: VpnClientsRequestEdit = Field(
        alias="vpn-clients",
        description="""VPN clients allowed to connect to this gateway.""",
    )
    vpn_domain: str = Field(
        alias="vpn-domain",
        description="""Gateway VPN domain identified by the name or UID.""",
    )
    vpn_domain_exclude_external_ip_addresses: bool = Field(
        alias="vpn-domain-exclude-external-ip-addresses",
        description="""Exclude the external IP addresses from the VPN domain of this Security Gateway.""",
    )
    vpn_domain_type: str = Field(
        alias="vpn-domain-type", description="""Gateway VPN domain type."""
    )
    enable_clientless_vpn: bool = Field(
        alias="enable-clientless-vpn",
        description="""Enable clientless VPN access for this gateway.""",
    )
    clientless_vpn_settings: ClientlessVpnSettingsRequestEdit = Field(
        alias="clientless-vpn-settings", description="""Clientless VPN Settings."""
    )
