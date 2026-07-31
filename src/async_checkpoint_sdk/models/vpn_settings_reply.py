from api_object_standard_identifier import ApiObjectStandardIdentifier
from authentication_reply import AuthenticationReply
from clientless_vpn_settings_reply import ClientlessVpnSettingsReply
from exported_routes_reply import ExportedRoutesReply
from link_selection_reply import LinkSelectionReply
from office_mode_reply import OfficeModeReply
from portal_reply import PortalReply
from pydantic import BaseModel, Field
from remote_access_reply import RemoteAccessReply
from vpn_advanced_reply import VpnAdvancedReply
from vpn_clients_reply import VpnClientsReply


class VpnSettingsReply(BaseModel):
    interfaces: list[dict] = Field(
        alias="interfaces", description="""Enhanced Link Selection Interfaces."""
    )
    advanced: VpnAdvancedReply = Field(alias="advanced", description="""Advanced VPN settings.""")
    authentication: AuthenticationReply = Field(
        alias="authentication", description="""Authentication."""
    )
    exported_routes: ExportedRoutesReply = Field(
        alias="exported-routes",
        description="""<html>Exported Routes.<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
    link_selection: LinkSelectionReply = Field(alias="link-selection", description="""N/A""")
    maximum_concurrent_ike_negotiations: int = Field(
        alias="maximum-concurrent-ike-negotiations", description="""N/A"""
    )
    maximum_concurrent_tunnels: int = Field(
        alias="maximum-concurrent-tunnels", description="""N/A"""
    )
    office_mode: OfficeModeReply = Field(alias="office-mode", description="""N/A""")
    remote_access: RemoteAccessReply = Field(alias="remote-access", description="""N/A""")
    saml_portal_settings: PortalReply = Field(
        alias="saml-portal-settings",
        description="""Configuration of the SAML portal for VPN authentication.""",
    )
    vpn_clients: VpnClientsReply = Field(
        alias="vpn-clients", description="""VPN clients allowed to connect to this gateway."""
    )
    vpn_domain: ApiObjectStandardIdentifier = Field(
        alias="vpn-domain", description="""Gateway VPN domain."""
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
    clientless_vpn_settings: ClientlessVpnSettingsReply = Field(
        alias="clientless-vpn-settings", description="""Clientless VPN Settings."""
    )
