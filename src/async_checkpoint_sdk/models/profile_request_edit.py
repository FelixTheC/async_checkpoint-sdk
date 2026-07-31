from .add import add
from .advanced_dns_settings_request_edit import AdvancedDnsSettingsRequestEdit
from .ips_settings_request import IpsSettingsRequest
from .ips_tag_category_request import IpsTagCategoryRequest
from .mail_settings_request_edit import MailSettingsRequestEdit
from .malicious_links_request import MaliciousLinksRequest
from .override_activation_by_protection_request import (
    OverrideActivationByProtectionRequest,
)
from .profile_indicator_override_request import ProfileIndicatorOverrideRequest
from .pydantic import BaseModel, Field
from .remove import remove


class ProfileRequestEdit(BaseModel):
    active_protections_performance_impact: str = Field(
        alias="active-protections-performance-impact",
        description="""Protections with this performance impact only will be activated in the profile.""",
    )
    active_protections_severity: str = Field(
        alias="active-protections-severity",
        description="""Protections with this severity only will be activated in the profile.""",
    )
    advanced_dns_settings: AdvancedDnsSettingsRequestEdit = Field(
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
    indicator_overrides: add | remove | ProfileIndicatorOverrideRequest | list[dict] = Field(
        alias="indicator-overrides",
        description="""Indicators whose action will be overridden in this profile.""",
    )
    ips_settings: IpsSettingsRequest = Field(
        alias="ips-settings", description="""IPS blade settings."""
    )
    malicious_mail_policy_settings: MailSettingsRequestEdit = Field(
        alias="malicious-mail-policy-settings",
        description="""Malicious Mail Policy for MTA Gateways.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    overrides: add | remove | OverrideActivationByProtectionRequest | list[dict] = Field(
        alias="overrides",
        description="""Overrides per profile for this protection.""",
    )
    scan_malicious_links: MaliciousLinksRequest = Field(
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
        alias="threat-extraction",
        description="""Is Threat Extraction blade activated.""",
    )
    zero_phishing: bool = Field(
        alias="zero-phishing", description="""Is Zero Phishing blade activated."""
    )
    activate_protections_by_extended_attributes: (
        add | remove | IpsTagCategoryRequest | list[dict]
    ) = Field(
        alias="activate-protections-by-extended-attributes",
        description="""Activate protections by these extended attributes.""",
    )
    deactivate_protections_by_extended_attributes: (
        add | remove | IpsTagCategoryRequest | list[dict]
    ) = Field(
        alias="deactivate-protections-by-extended-attributes",
        description="""Deactivate protections by these extended attributes.""",
    )
    use_extended_attributes: bool = Field(
        alias="use-extended-attributes",
        description="""Whether to activate/deactivate IPS protections according to the extended attributes.""",
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
    tags: add | remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
