from .advanced_cluster_settings_request import AdvancedClusterSettingsRequest
from .advanced_settings_request import AdvancedSettingsRequest
from .appi_settings_request import AppiSettingsRequest
from .comm_with_server_behind_nat_settings_request import (
    CommWithServerBehindNatSettingsRequest,
)
from .firewall_settings_request import FirewallSettingsRequest
from .identity_awareness_settings_request_new import IdentityAwarenessSettingsRequestNew
from .ips_settings_cluster_request_new import IpsSettingsClusterRequestNew
from .logs_settings_request import LogsSettingsRequest
from .nat_settings_gateway_cluster_request import NatSettingsGatewayClusterRequest
from .object import Object
from .platform_portal_request_new import PlatformPortalRequestNew
from .proxy_settings_request import ProxySettingsRequest
from .pydantic import BaseModel, Field
from .ssl_inspection_request import SslInspectionRequest
from .user_check_portal_request_new import UserCheckPortalRequestNew
from .vpn_settings_request_new import VpnSettingsRequestNew
from .zero_phishing_fqdn_settings_request import ZeroPhishingFqdnSettingsRequest


class ClusterRequestNew(BaseModel):
    advanced_settings: AdvancedSettingsRequest = Field(
        alias="advanced-settings", description="""N/A"""
    )
    anti_bot: bool = Field(alias="anti-bot", description="""Anti-Bot blade enabled.""")
    anti_spam_and_email_security: bool = Field(
        alias="anti-spam-and-email-security",
        description="""Enables Anti-Spam & Email-Security blade.""",
    )
    anti_virus: bool = Field(alias="anti-virus", description="""Anti-Virus blade enabled.""")
    application_control: bool = Field(
        alias="application-control",
        description="""Application Control blade enabled.""",
    )
    application_control_and_url_filtering_settings: AppiSettingsRequest = Field(
        alias="application-control-and-url-filtering-settings",
        description="""Gateway Application Control and URL filtering settings.""",
    )
    auto_topology_custom_recalculation_time: int = Field(
        alias="auto-topology-custom-recalculation-time",
        description="""Auto topology custom recalculation time (seconds).""",
    )
    auto_topology_use_custom_recalculation_time: bool = Field(
        alias="auto-topology-use-custom-recalculation-time",
        description="""Auto topology to use custom recalculation time instead of default.""",
    )
    cluster_mode: str = Field(alias="cluster-mode", description="""Cluster mode.""")
    cluster_settings: AdvancedClusterSettingsRequest = Field(
        alias="cluster-settings", description="""ClusterXL and VRRP Settings."""
    )
    communication_with_servers_behind_nat: CommWithServerBehindNatSettingsRequest = Field(
        alias="communication-with-servers-behind-nat",
        description="""Gateway behind NAT communications settings with the server.""",
    )
    content_awareness: bool = Field(
        alias="content-awareness", description="""Content Awareness blade enabled."""
    )
    data_loss_prevention: bool = Field(
        alias="data-loss-prevention", description="""Data Loss Prevention blade."""
    )
    enable_https_inspection: bool = Field(
        alias="enable-https-inspection",
        description="""Enable HTTPS Inspection after defining an outbound inspection certificate. <br>To define the outbound certificate use outbound inspection certificate API.""",
    )
    fetch_policy: str | list[str] = Field(
        alias="fetch-policy",
        description="""Security management server(s) to fetch the policy from.""",
    )
    firewall: bool = Field(alias="firewall", description="""Firewall blade enabled.""")
    firewall_settings: FirewallSettingsRequest = Field(
        alias="firewall-settings", description="""N/A"""
    )
    geo_mode: bool = Field(
        alias="geo-mode",
        description="""Cluster High Availability Geo mode.<br>This setting applies only to a cluster deployed in a cloud. Available when the cluster mode equals cluster-xl-ha.""",
    )
    hardware: str = Field(alias="hardware", description="""Cluster platform hardware.""")
    hit_count: bool = Field(
        alias="hit-count",
        description="""Hit count tracks the number of connections each rule matches.""",
    )
    https_inspection: SslInspectionRequest = Field(
        alias="https-inspection", description="""HTTPS inspection."""
    )
    identity_awareness: bool = Field(
        alias="identity-awareness", description="""Identity awareness blade enabled."""
    )
    identity_awareness_settings: IdentityAwarenessSettingsRequestNew = Field(
        alias="identity-awareness-settings",
        description="""Gateway Identity Awareness settings.""",
    )
    interfaces: list[dict] = Field(alias="interfaces", description="""Cluster interfaces.""")
    ips: bool = Field(alias="ips", description="""Intrusion Prevention System blade enabled.""")
    ips_settings: IpsSettingsClusterRequestNew = Field(
        alias="ips-settings", description="""Cluster IPS settings."""
    )
    ips_update_policy: str = Field(
        alias="ips-update-policy",
        description="""Specifies whether the IPS will be downloaded from .the Management or directly to the Gateway.""",
    )
    members: list[dict] = Field(
        alias="members",
        description="""Cluster members list. Only new cluster member can be added. Adding existing gateway is not supported.""",
    )
    mobile_access: bool = Field(alias="mobile-access", description="""Mobile Access blade.""")
    monitoring: bool = Field(
        alias="monitoring", description="""Enables Real Time Monitoring blade."""
    )
    nat_hide_internal_interfaces: bool = Field(
        alias="nat-hide-internal-interfaces",
        description="""Hide internal networks behind the Gateway's external IP.""",
    )
    nat_settings: NatSettingsGatewayClusterRequest = Field(
        alias="nat-settings", description="""NAT settings."""
    )
    os_name: str = Field(alias="os-name", description="""Cluster platform operating system.""")
    platform_portal_settings: PlatformPortalRequestNew = Field(
        alias="platform-portal-settings", description="""Platform portal settings."""
    )
    proxy_settings: ProxySettingsRequest = Field(
        alias="proxy-settings", description="""Proxy Server for Gateway."""
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
    send_alerts_to_server: Object = Field(
        alias="send-alerts-to-server", description="""Server(s) to send alerts to."""
    )
    send_logs_to_backup_server: Object = Field(
        alias="send-logs-to-backup-server",
        description="""Backup server(s) to send logs to.""",
    )
    send_logs_to_server: Object = Field(
        alias="send-logs-to-server", description="""Server(s) to send logs to."""
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
    url_filtering: bool = Field(
        alias="url-filtering", description="""URL Filtering blade enabled."""
    )
    usercheck_portal_settings: UserCheckPortalRequestNew = Field(
        alias="usercheck-portal-settings", description="""UserCheck portal settings."""
    )
    version: str = Field(alias="version", description="""Cluster platform version.""")
    vpn: bool = Field(alias="vpn", description="""VPN blade enabled.""")
    vpn_settings: VpnSettingsRequestNew = Field(
        alias="vpn-settings", description="""Gateway VPN settings."""
    )
    zero_phishing: bool = Field(
        alias="zero-phishing", description="""Zero Phishing blade enabled."""
    )
    zero_phishing_settings: ZeroPhishingFqdnSettingsRequest = Field(
        alias="zero-phishing-settings", description="""Fqdn settings."""
    )
    logs_settings: LogsSettingsRequest = Field(
        alias="logs-settings",
        description="""Logs settings that apply to Quantum Security Gateways that run Gaia OS.""",
    )
    show_portals_certificate: bool = Field(
        alias="show-portals-certificate",
        description="""Indicates whether to show the portals certificate value in the reply.""",
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    groups: Object = Field(alias="groups", description="""Collection of group identifiers.""")
    tags: Object = Field(alias="tags", description="""Collection of tag identifiers.""")
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
