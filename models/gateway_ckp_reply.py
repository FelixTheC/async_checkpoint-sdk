from advanced_settings_reply import AdvancedSettingsReply
from api_domain_identifier import ApiDomainIdentifier
from appi_settings_reply import AppiSettingsReply
from available_actions_reply import AvailableActionsReply
from comm_with_server_behind_nat_settings_reply import (
    CommWithServerBehindNatSettingsReply,
)
from firewall_settings_reply import FirewallSettingsReply
from identity_awareness_settings_reply import IdentityAwarenessSettingsReply
from ips_settings_reply import IpsSettingsReply
from logs_settings_reply import LogsSettingsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from nat_settings_gateway_cluster_reply import NatSettingsGatewayClusterReply
from portal_reply import PortalReply
from proxy_settings_reply import ProxySettingsReply
from pydantic import BaseModel, Field
from smb_logs_settings_reply import SmbLogsSettingsReply
from ssl_inspection_reply import SslInspectionReply
from trust_details_reply import TrustDetailsReply
from vpn_settings_reply import VpnSettingsReply
from zero_phishing_fqdn_settings_reply import ZeroPhishingFqdnSettingsReply


class GatewayCkpReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    advanced_settings: AdvancedSettingsReply = Field(
        alias="advanced-settings", description="""N/A"""
    )
    anti_bot: bool = Field(alias="anti-bot", description="""Anti-Bot blade enabled.""")
    anti_spam_and_email_security: bool = Field(
        alias="anti-spam-and-email-security",
        description="""Anti-Spam & Email-Security blade enabled.""",
    )
    anti_virus: bool = Field(
        alias="anti-virus", description="""Anti-Virus blade enabled."""
    )
    application_control: bool = Field(
        alias="application-control",
        description="""Application Control blade enabled.""",
    )
    application_control_and_url_filtering_settings: AppiSettingsReply = Field(
        alias="application-control-and-url-filtering-settings",
        description="""Gateway Application Control and URL filtering settings.""",
    )
    auto_generate_ip: bool = Field(
        alias="auto-generate-ip",
        description="""Use an automatically generated IP address for the Gateway object (applies only to Smart-1 Cloud).""",
    )
    auto_topology_custom_recalculation_time: int = Field(
        alias="auto-topology-custom-recalculation-time",
        description="""Auto topology custom recalculation time (seconds).""",
    )
    auto_topology_use_custom_recalculation_time: bool = Field(
        alias="auto-topology-use-custom-recalculation-time",
        description="""Auto topology to use custom recalculation time instead of default.""",
    )
    autonomous_system_number: str = Field(
        alias="autonomous-system-number",
        description="""The Autonomous System Number (ASN) for this Check Point Security Gateway.""",
    )
    communication_with_servers_behind_nat: CommWithServerBehindNatSettingsReply = Field(
        alias="communication-with-servers-behind-nat",
        description="""Gateway behind NAT communications settings with the server.""",
    )
    content_awareness: bool = Field(
        alias="content-awareness", description="""Content Awareness blade enabled."""
    )
    data_loss_prevention: bool = Field(
        alias="data-loss-prevention", description="""Data Loss Prevention."""
    )
    dynamic_ip: bool = Field(alias="dynamic-ip", description="""Dynamic IP address.""")
    enable_https_inspection: bool = Field(
        alias="enable-https-inspection",
        description="""Enable HTTPS Inspection after defining an outbound inspection certificate. <br>To define the outbound certificate use set outbound-inspection-certificate.""",
    )
    externally_managed: bool = Field(
        alias="externally-managed",
        description="""Externally Managed Check Point Gateway.""",
    )
    fetch_policy: list[str] = Field(
        alias="fetch-policy",
        description="""Security management server(s) to fetch the policy from.""",
    )
    firewall: bool = Field(alias="firewall", description="""Firewall blade enabled.""")
    firewall_settings: FirewallSettingsReply = Field(
        alias="firewall-settings", description="""N/A"""
    )
    groups: list[dict] = Field(
        alias="groups",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    hardware: str = Field(
        alias="hardware", description="""Gateway platform hardware type."""
    )
    hardware_subtype: str = Field(
        alias="hardware-subtype",
        description="""Gateway type (relevant only for Spark gateways).""",
    )
    hit_count: bool = Field(
        alias="hit-count",
        description="""Hit count tracks the number of connections each rule matches.""",
    )
    https_inspection: SslInspectionReply = Field(
        alias="https-inspection", description="""HTTPS inspection."""
    )
    icap_server: bool = Field(
        alias="icap-server", description="""ICAP Server enabled."""
    )
    identity_awareness: bool = Field(
        alias="identity-awareness", description="""Identity awareness blade enabled."""
    )
    identity_awareness_settings: IdentityAwarenessSettingsReply = Field(
        alias="identity-awareness-settings",
        description="""Gateway Identity Awareness settings.""",
    )
    interfaces: list[dict] = Field(
        alias="interfaces", description="""Network interfaces."""
    )
    interfaces_topology_settings: str = Field(
        alias="interfaces-topology-settings",
        description="""Topology setting for all interfaces on a Security Gateway.
Default for Security Gateways that run Gaia OS: 'per interface'.
Default for Quantum Spark gateways that run Gaia Embedded OS: 'global and automatic'.
Changing this setting is supported only for Quantum Spark gateways.""",
    )
    ips: bool = Field(
        alias="ips", description="""Intrusion Prevention System blade enabled."""
    )
    ips_settings: IpsSettingsReply = Field(
        alias="ips-settings", description="""Gateway Ips settings."""
    )
    ips_update_policy: str = Field(
        alias="ips-update-policy",
        description="""Specifies whether the IPS will be downloaded from the Management or directly to the Gateway.""",
    )
    ipv4_address: str = Field(alias="ipv4-address", description="""IPv4 address.""")
    ipv6_address: str = Field(alias="ipv6-address", description="""IPv6 address.""")
    legacy_url_filtering: bool = Field(
        alias="legacy-url-filtering", description="""Legacy URL Filtering enabled."""
    )
    log_server: bool = Field(alias="log-server", description="""Logging & Status.""")
    mobile_access: bool = Field(
        alias="mobile-access", description="""Mobile-Access blade enabled."""
    )
    monitoring: bool = Field(
        alias="monitoring", description="""Monitoring blade enabled."""
    )
    nat_hide_internal_interfaces: bool = Field(
        alias="nat-hide-internal-interfaces",
        description="""Hide internal networks behind the Gateway's external IP.""",
    )
    nat_settings: NatSettingsGatewayClusterReply = Field(
        alias="nat-settings", description="""NAT settings."""
    )
    network_policy_management: bool = Field(
        alias="network-policy-management", description="""Management blade enabled."""
    )
    os_name: str = Field(
        alias="os-name", description="""Gateway platform operating system."""
    )
    platform_portal_settings: PortalReply = Field(
        alias="platform-portal-settings", description="""Platform portal settings."""
    )
    policy_server: bool = Field(
        alias="policy-server", description="""Policy-Server blade enabled."""
    )
    proxy_settings: ProxySettingsReply = Field(
        alias="proxy-settings", description="""N/A"""
    )
    qos: bool = Field(alias="qos", description="""QoS.""")
    rtm_counters_report: bool = Field(
        alias="rtm-counters-report",
        description="""Enables monitoring blades system counters report (e.g CPU Usage,Memory Usage).""",
    )
    rtm_traffic_report: bool = Field(
        alias="rtm-traffic-report",
        description="""Enables monitoring blades traffic report.""",
    )
    rtm_traffic_report_per_connection: bool = Field(
        alias="rtm-traffic-report-per-connection",
        description="""Enables Monitoring blade traffic report per connection.""",
    )
    save_logs_locally: bool = Field(
        alias="save-logs-locally", description="""Save logs locally on the gateway."""
    )
    send_alerts_to_server: list[str] = Field(
        alias="send-alerts-to-server", description="""Server(s) to send alerts to."""
    )
    send_logs_to_backup_server: list[str] = Field(
        alias="send-logs-to-backup-server",
        description="""Backup server(s) to send logs to.""",
    )
    send_logs_to_server: list[str] = Field(
        alias="send-logs-to-server", description="""Servers(s) to send logs to."""
    )
    sic_message: str = Field(
        alias="sic-message", description="""Secure Internal Communication message."""
    )
    sic_name: str = Field(
        alias="sic-name", description="""Secure Internal Communication name."""
    )
    sic_state: str = Field(
        alias="sic-state", description="""Secure Internal Communication state."""
    )
    threat_emulation: bool = Field(
        alias="threat-emulation", description="""Threat Emulation blade enabled."""
    )
    threat_extraction: bool = Field(
        alias="threat-extraction", description="""Threat Extraction blade enabled."""
    )
    threat_prevention_mode: str = Field(
        alias="threat-prevention-mode",
        description="""The mode of Threat Prevention to use. When using Autonomous Threat Prevention, disabling the Threat Prevention blades is not allowed.""",
    )
    trust_details: TrustDetailsReply = Field(
        alias="trust-details", description="""Details for trusted communication."""
    )
    trust_method: str = Field(
        alias="trust-method",
        description="""Trust method that was used for establishing communication.""",
    )
    url_filtering: bool = Field(
        alias="url-filtering", description="""URL Filtering blade enabled."""
    )
    usercheck_portal_settings: PortalReply = Field(
        alias="usercheck-portal-settings", description="""UserCheck portal settings."""
    )
    version: str = Field(alias="version", description="""Gateway platform version.""")
    vpn: bool = Field(alias="vpn", description="""VPN blade enabled.""")
    vpn_settings: VpnSettingsReply = Field(
        alias="vpn-settings", description="""Gateway VPN settings."""
    )
    zero_phishing: bool = Field(
        alias="zero-phishing", description="""Zero Phishing blade enabled."""
    )
    zero_phishing_settings: ZeroPhishingFqdnSettingsReply = Field(
        alias="zero-phishing-settings", description="""Fqdn settings."""
    )
    logs_settings: LogsSettingsReply = Field(
        alias="logs-settings",
        description="""Logs settings that apply to Quantum Security Gateways that run Gaia OS.""",
    )
    smb_logs_settings: SmbLogsSettingsReply = Field(
        alias="smb-logs-settings",
        description="""Logs settings that apply to Quantum Spark Appliances that run Gaia Embedded OS.""",
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
