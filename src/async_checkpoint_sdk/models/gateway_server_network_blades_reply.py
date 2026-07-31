from .pydantic import BaseModel, Field


class GatewayServerNetworkBladesReply(BaseModel):
    firewall: bool = Field(alias="firewall", description="""Firewall blade.""")
    anti_bot: bool = Field(alias="anti-bot", description="""Anti-Bot blade.""")
    anti_spam: bool = Field(alias="anti-spam", description="""Anti-Spam & Email Security blade.""")
    anti_virus: bool = Field(alias="anti-virus", description="""Anti-Virus blade.""")
    application_control: bool = Field(
        alias="application-control", description="""Application control blade."""
    )
    content_awareness: bool = Field(
        alias="content-awareness", description="""Content awareness blade."""
    )
    data_loss_prevention: bool = Field(
        alias="data-loss-prevention", description="""Data loss prevention blade."""
    )
    identity_awareness: bool = Field(
        alias="identity-awareness", description="""Identity awareness blade."""
    )
    ips: bool = Field(alias="ips", description="""IPS blade.""")
    mobile_access: bool = Field(alias="mobile-access", description="""Mobile access blade.""")
    monitoring: bool = Field(alias="monitoring", description="""Monitoring blade.""")
    qos: bool = Field(alias="qos", description="""QoS blade.""")
    site_to_site_vpn: bool = Field(
        alias="site-to-site-vpn", description="""Site to site VPN blade."""
    )
    threat_emulation: bool = Field(
        alias="threat-emulation", description="""Threat emulation blade."""
    )
    threat_extraction: bool = Field(
        alias="threat-extraction", description="""Threat extraction blade."""
    )
    traditional_anti_virus: bool = Field(
        alias="traditional-anti-virus", description="""Traditional Anti-Virus blade."""
    )
    url_filtering: bool = Field(alias="url-filtering", description="""URL filtering blade.""")
    zero_phishing: bool = Field(alias="zero-phishing", description="""Zero phishing blade.""")
