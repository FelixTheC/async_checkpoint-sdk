from .pydantic import BaseModel, Field


class HarmonyMobileReply(BaseModel):
    protect_policy_enabled: bool = Field(
        alias="protect-policy-enabled",
        description="""Enable/disable Protect Application- cannot be enable if Harmony SDK is enable.""",
    )
    protect_high_risk_action: str = Field(
        alias="protect-high-risk-action",
        description="""What is the action if there is high risk found by Harmony Mobile.""",
    )
    protect_high_risk_message: str = Field(
        alias="protect-high-risk-message",
        description="""The message can contain only English characters, digits, comma, spaces and points.""",
    )
    protect_medium_risk_action: str = Field(
        alias="protect-medium-risk-action",
        description="""What is the action if there is medium risk found by Harmony Mobile.""",
    )
    protect_medium_risk_message: str = Field(
        alias="protect-medium-risk-message",
        description="""The message can contain only English characters, digits, comma, spaces and points.""",
    )
    protect_not_activated_action: str = Field(
        alias="protect-not-activated-action",
        description="""What is the action if there is policy violation (configuration for Harmony Mobile).""",
    )
    protect_not_activated_message: str = Field(
        alias="protect-not-activated-message",
        description="""The message can contain only English characters, digits, comma, spaces and points.""",
    )
    enable_harmony_mobile_sdk: bool = Field(
        alias="enable-harmony-mobile-sdk",
        description="""Enable/disable Harmony SDK - cannot be enable if Harmony Mobile Application is enable.""",
    )
    compromised_behavior: str = Field(
        alias="compromised-behavior",
        description="""Device configuration enables/disable malicious behavior (configuration for Harmony SDK).""",
    )
    harmony_mobile_sdk_license: str = Field(
        alias="harmony-mobile-sdk-license",
        description="""License for Harmony Mobile Sdk (configuration for Harmony SDK).""",
    )
    malware_behavior: str = Field(
        alias="malware-behavior",
        description="""Behavior when App is identified as malicious (configuration for Harmony SDK).""",
    )
    man_in_the_middle_attack: str = Field(
        alias="man-in-the-middle-attack",
        description="""Behavior when there is a network man-in-the-middle attack (configuration for Harmony SDK).""",
    )
    os_integrity_compromised: str = Field(
        alias="os-integrity-compromised",
        description="""Behavior when Device OS is compromised (configuration for Harmony SDK).""",
    )
    suspicious_app: str = Field(
        alias="suspicious-app",
        description="""Behavior when App is suspected as malicious (configuration for Harmony SDK).""",
    )
    suspicious_enterprise_certificate: str = Field(
        alias="suspicious-enterprise-certificate",
        description="""Behavior when a certificate profile has been installed allowing the installing of apps on device from .unknown source - iOS only (configuration for Harmony SDK).""",
    )
