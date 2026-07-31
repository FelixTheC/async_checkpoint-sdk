from advanced_dns_settings_reply import AdvancedDnsSettingsReply
from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from ips_settings_reply import IpsSettingsReply
from mail_settings_reply import MailSettingsReply
from malicious_links_reply import MaliciousLinksReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class ProfileReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    active_protections_performance_impact: str = Field(
        alias="active-protections-performance-impact",
        description="""Protections with this performance impact only will be activated in the profile.""",
    )
    active_protections_severity: str = Field(
        alias="active-protections-severity",
        description="""Protections with this severity only will be activated in the profile.""",
    )
    advanced_dns_settings: AdvancedDnsSettingsReply = Field(
        alias="advanced-dns-settings", description="""Advanced DNS Settings."""
    )
    confidence_level_high: str = Field(
        alias="confidence-level-high",
        description="""Action for protections with high confidence level.""",
    )
    confidence_level_low: str = Field(
        alias="confidence-level-low",
        description="""Action for protections with low confidence level.""",
    )
    confidence_level_medium: str = Field(
        alias="confidence-level-medium",
        description="""Action for protections with medium confidence level.""",
    )
    indicator_overrides: list[dict] = Field(
        alias="indicator-overrides",
        description="""Indicators whose action will be overridden in this profile.""",
    )
    ips_settings: IpsSettingsReply = Field(
        alias="ips-settings", description="""IPS blade settings."""
    )
    malicious_mail_policy_settings: MailSettingsReply = Field(
        alias="malicious-mail-policy-settings",
        description="""Malicious Mail Policy for MTA Gateways.""",
    )
    overrides: list[dict] = Field(
        alias="overrides", description="""Overrides per profile for this protection."""
    )
    scan_malicious_links: MaliciousLinksReply = Field(
        alias="scan-malicious-links",
        description="""Scans malicious links (URLs) inside email messages.""",
    )
    use_indicators: bool = Field(
        alias="use-indicators",
        description="""Indicates whether the profile should make use of indicators.""",
    )
    anti_bot: bool = Field(alias="anti-bot", description="""Is Anti-Bot blade activated.""")
    anti_virus: bool = Field(alias="anti-virus", description="""Is Anti-Virus blade activated.""")
    ips: bool = Field(alias="ips", description="""Is IPS blade activated.""")
    threat_emulation: bool = Field(
        alias="threat-emulation", description="""Is Threat Emulation blade activated."""
    )
    threat_extraction: bool = Field(
        alias="threat-extraction", description="""Is Threat Extraction blade activated."""
    )
    zero_phishing: bool = Field(
        alias="zero-phishing", description="""Is Zero Phishing blade activated."""
    )
    extended_attributes_to_activate: list[dict] = Field(
        alias="extended-attributes-to-activate",
        description="""Activate protections by these extended attributes.""",
    )
    extended_attributes_to_deactivate: list[dict] = Field(
        alias="extended-attributes-to-deactivate",
        description="""Deactivate protections by these extended attributes.""",
    )
    use_extended_attributes: bool = Field(
        alias="use-extended-attributes",
        description="""Whether to activate/deactivate IPS protections according to the extended attributes.""",
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain", description="""Information about the domain that holds the Object."""
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
        alias="available-actions", description="""Actions that are available on the object."""
    )
