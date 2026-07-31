from advanced_settings_reply import AdvancedSettingsReply
from api_domain_identifier import ApiDomainIdentifier
from appi_settings_reply import AppiSettingsReply
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from nat_settings_gateway_cluster_reply import NatSettingsGatewayClusterReply
from proxy_settings_reply import ProxySettingsReply
from pydantic import BaseModel, Field
from ssl_inspection_reply import SslInspectionReply


class LsmGwProfileReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    advanced_settings: AdvancedSettingsReply = Field(
        alias="advanced-settings", description="""N/A"""
    )
    anti_bot: bool = Field(alias="anti-bot", description="""Anti-Bot blade enabled.""")
    anti_virus: bool = Field(
        alias="anti-virus", description="""Anti-Virus blade enabled."""
    )
    application_control: bool = Field(
        alias="application-control",
        description="""Application Control blade enabled.""",
    )
    application_control_and_url_filtering_settings: AppiSettingsReply = Field(
        alias="application-control-and-url-filtering-settings",
        description="""Gateway Application Control and URL Filtering settings.""",
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
    firewall: bool = Field(alias="firewall", description="""Firewall blade enabled.""")
    groups: list[dict] = Field(
        alias="groups",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    hit_count: bool = Field(
        alias="hit-count",
        description="""Hit count tracks the number of connections each rule matches.""",
    )
    https_inspection: SslInspectionReply = Field(
        alias="https-inspection", description="""HTTPS inspection."""
    )
    interfaces: list[str] = Field(
        alias="interfaces", description="""Cluster network interfaces."""
    )
    ips: bool = Field(
        alias="ips", description="""Intrusion Prevention System blade enabled."""
    )
    nat_hide_internal_interfaces: bool = Field(
        alias="nat-hide-internal-interfaces",
        description="""Hide internal networks behind the Gateway's external IP.""",
    )
    nat_settings: NatSettingsGatewayClusterReply = Field(
        alias="nat-settings", description="""NAT settings."""
    )
    os_name: str = Field(
        alias="os-name", description="""Gateway platform operating system."""
    )
    proxy_settings: ProxySettingsReply = Field(
        alias="proxy-settings", description="""N/A"""
    )
    qos: bool = Field(alias="qos", description="""QoS.""")
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
    version: str = Field(alias="version", description="""Gateway platform version.""")
    vpn: bool = Field(alias="vpn", description="""VPN blade enabled.""")
    zero_phishing: bool = Field(
        alias="zero-phishing", description="""Zero Phishing blade enabled."""
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
