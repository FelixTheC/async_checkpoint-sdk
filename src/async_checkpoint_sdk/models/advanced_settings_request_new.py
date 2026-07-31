from .otp_settings_request_new import OtpSettingsRequestNew
from .pydantic import BaseModel, Field


class AdvancedSettingsRequestNew(BaseModel):
    dynamic_id_message: str = Field(
        alias="dynamic-id-message",
        description="""Dynamic ID message displayed to users.""",
    )
    otp_settings: OtpSettingsRequestNew = Field(
        alias="otp-settings",
        description="""OTP (One Time Password) configuration settings.""",
    )
    enable_display_user_details: bool = Field(
        alias="enable-display-user-details",
        description="""Enable display of user details.""",
    )
    country_code: str = Field(
        alias="country-code", description="""Country code for SMS services."""
    )
    user_details_retrieval: str = Field(
        alias="user-details-retrieval", description="""User details retrieval method."""
    )
