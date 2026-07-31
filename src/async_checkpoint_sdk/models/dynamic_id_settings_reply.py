from advanced_settings_reply import AdvancedSettingsReply
from pydantic import BaseModel, Field
from sms_provider_credentials_reply import SmsProviderCredentialsReply


class DynamicIdSettingsReply(BaseModel):
    sms_provider_and_email_settings: str = Field(
        alias="sms-provider-and-email-settings",
        description="""SMS provider and email configuration.""",
    )
    sms_provider_credentials: SmsProviderCredentialsReply = Field(
        alias="sms-provider-credentials", description="""SMS provider credentials configuration."""
    )
    advanced_settings: AdvancedSettingsReply = Field(
        alias="advanced-settings", description="""Advanced Dynamic ID configuration settings."""
    )
