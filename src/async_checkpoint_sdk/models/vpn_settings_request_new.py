from .authentication_request_new import AuthenticationRequestNew
from .clientless_vpn_settings_request_new import ClientlessVpnSettingsRequestNew
from .exported_routes_request_new import ExportedRoutesRequestNew
from .link_selection_request_new import LinkSelectionRequestNew
from .office_mode_request import OfficeModeRequest
from .pydantic import BaseModel, Field
from .remote_access_request import RemoteAccessRequest
from .saml_portal_request_new import SamlPortalRequestNew
from .vpn_advanced_request_new import VpnAdvancedRequestNew
from .vpn_certificate_request import VpnCertificateRequest
from .vpn_clients_request_new import VpnClientsRequestNew


class VpnSettingsRequestNew(BaseModel):
    advanced: VpnAdvancedRequestNew = Field(
        alias="advanced", description="""Advanced VPN settings."""
    )
    authentication: AuthenticationRequestNew = Field(
        alias="authentication", description="""Authentication."""
    )
    certificates: VpnCertificateRequest = Field(
        alias="certificates", description="""Vpn certificates."""
    )
    exported_routes: ExportedRoutesRequestNew = Field(
        alias="exported-routes",
        description="""<html>Exported Routes.<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
    link_selection: LinkSelectionRequestNew = Field(
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
    saml_portal_settings: SamlPortalRequestNew = Field(
        alias="saml-portal-settings",
        description="""Configuration of the SAML portal for VPN authentication.""",
    )
    vpn_clients: VpnClientsRequestNew = Field(
        alias="vpn-clients",
        description="""VPN clients allowed to connect to this gateway.""",
    )
    vpn_domain: str = Field(
        alias="vpn-domain",
        description="""Gateway VPN domain identified by the name or UID.""",
    )
    vpn_domain_exclude_external_ip_addresses: bool = Field(
        alias="vpn-domain-exclude-external-ip-addresses",
        description="""Exclude the external IP addresses from .the VPN domain of this Security Gateway.""",
    )
    vpn_domain_type: str = Field(
        alias="vpn-domain-type", description="""Gateway VPN domain type."""
    )
    enable_clientless_vpn: bool = Field(
        alias="enable-clientless-vpn",
        description="""Enable clientless VPN access for this gateway.""",
    )
    clientless_vpn_settings: ClientlessVpnSettingsRequestNew = Field(
        alias="clientless-vpn-settings", description="""Clientless VPN Settings."""
    )
