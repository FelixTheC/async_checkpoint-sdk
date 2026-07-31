from .advanced_settings_request_new import AdvancedSettingsRequestNew
from .pydantic import BaseModel, Field
from .sms_provider_credentials_request import SmsProviderCredentialsRequest


class DynamicIdSettingsRequestNew(BaseModel):
    sms_provider_and_email_settings: str = Field(
        alias="sms-provider-and-email-settings",
        description="""SMS provider and email configuration.""",
    )
    sms_provider_credentials: SmsProviderCredentialsRequest = Field(
        alias="sms-provider-credentials",
        description="""SMS provider credentials configuration.""",
    )
    advanced_settings: AdvancedSettingsRequestNew = Field(
        alias="advanced-settings",
        description="""Advanced Dynamic ID configuration settings.""",
    )
