from .appi_settings_request import AppiSettingsRequest
from .identity_awareness_settings_request_edit import (
    IdentityAwarenessSettingsRequestEdit,
)
from .object import Object
from .pydantic import BaseModel, Field
from .user_check_portal_request import UserCheckPortalRequest
from .vpn_settings_request import VpnSettingsRequest


class LegacyVirtualSystemRequestEdit(BaseModel):
    anti_bot: bool = Field(alias="anti-bot", description="""Anti-Bot blade enabled.""")
    anti_virus: bool = Field(alias="anti-virus", description="""Anti-Virus blade enabled.""")
    application_control: bool = Field(
        alias="application-control",
        description="""Application Control blade enabled.""",
    )
    application_control_and_url_filtering_settings: AppiSettingsRequest = Field(
        alias="application-control-and-url-filtering-settings",
        description="""Gateway Application Control and URL filtering settings.""",
    )
    content_awareness: bool = Field(
        alias="content-awareness", description="""Content Awareness blade enabled."""
    )
    identity_awareness: bool = Field(
        alias="identity-awareness", description="""Identity awareness blade enabled."""
    )
    identity_awareness_settings: IdentityAwarenessSettingsRequestEdit = Field(
        alias="identity-awareness-settings",
        description="""Gateway Identity Awareness settings.""",
    )
    ips: bool = Field(alias="ips", description="""Intrusion Prevention System blade enabled.""")
    ips_update_policy: str = Field(
        alias="ips-update-policy",
        description="""Specifies whether the IPS will be downloaded from .the Management or directly to the Gateway.""",
    )
    qos: bool = Field(alias="qos", description="""QoS.""")
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
    usercheck_portal_settings: UserCheckPortalRequest = Field(
        alias="usercheck-portal-settings", description="""UserCheck portal settings."""
    )
    vpn: bool = Field(alias="vpn", description="""VPN blade enabled.""")
    vpn_settings: VpnSettingsRequest = Field(
        alias="vpn-settings", description="""Gateway VPN settings."""
    )
    zero_phishing: bool = Field(
        alias="zero-phishing", description="""Zero Phishing blade enabled."""
    )
    zero_phishing_fqdn: str = Field(
        alias="zero-phishing-fqdn", description="""Zero Phishing gateway FQDN."""
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
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from .the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
    )
    tags: Object = Field(alias="tags", description="""Collection of tag identifiers.""")
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
