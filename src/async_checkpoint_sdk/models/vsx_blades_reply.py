from appi_settings_reply import AppiSettingsReply
from identity_awareness_settings_reply import IdentityAwarenessSettingsReply
from pydantic import BaseModel, Field
from vpn_settings_reply import VpnSettingsReply


class VsxBladesReply(BaseModel):
    anti_bot: bool = Field(alias="anti-bot", description="""Anti-Bot blade enabled.""")
    anti_virus: bool = Field(alias="anti-virus", description="""Anti-Virus blade enabled.""")
    application_control: bool = Field(
        alias="application-control", description="""Application Control blade enabled."""
    )
    application_control_and_url_filtering_settings: AppiSettingsReply = Field(
        alias="application-control-and-url-filtering-settings",
        description="""Gateway Application Control and URL filtering settings.""",
    )
    content_awareness: bool = Field(
        alias="content-awareness", description="""Content Awareness blade enabled."""
    )
    data_loss_prevention: bool = Field(
        alias="data-loss-prevention", description="""Data loss prevention blade."""
    )
    identity_awareness: bool = Field(
        alias="identity-awareness", description="""Identity awareness blade enabled."""
    )
    identity_awareness_settings: IdentityAwarenessSettingsReply = Field(
        alias="identity-awareness-settings", description="""Gateway Identity Awareness settings."""
    )
    ips: bool = Field(alias="ips", description="""Intrusion Prevention System blade enabled.""")
    ips_update_policy: str = Field(
        alias="ips-update-policy",
        description="""Specifies whether the IPS will be downloaded from the Management or directly to the Gateway.""",
    )
    monitoring: bool = Field(alias="monitoring", description="""Monitoring blade.""")
    qos: bool = Field(alias="qos", description="""QoS.""")
    site_to_site_vpn: bool = Field(alias="site-to-site-vpn", description="""VPN blade enabled.""")
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
    vpn_settings: VpnSettingsReply = Field(
        alias="vpn-settings", description="""Gateway VPN settings."""
    )
    zero_phishing: bool = Field(
        alias="zero-phishing", description="""Zero Phishing blade enabled."""
    )
    zero_phishing_fqdn: str = Field(
        alias="zero-phishing-fqdn", description="""Zero Phishing gateway FQDN."""
    )
