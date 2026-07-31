from client_display_settings_reply import ClientDisplaySettingsReply
from dynamic_id_settings_reply import DynamicIdSettingsReply
from identity_provider_settings_reply import IdentityProviderSettingsReply
from personal_certificate_settings_reply import PersonalCertificateSettingsReply
from pydantic import BaseModel, Field
from radius_settings_reply import RadiusSettingsReply
from secur_id_settings_reply import SecurIdSettingsReply


class AuthenticationMethodReply(BaseModel):
    authentication_factor: str = Field(
        alias="authentication-factor", description="""Type of authentication factor."""
    )
    personal_certificate: PersonalCertificateSettingsReply = Field(
        alias="personal-certificate",
        description="""Personal certificate authentication settings, relevant when authentication-factor is set to personal-certificate.""",
    )
    radius: RadiusSettingsReply = Field(
        alias="radius",
        description="""RADIUS authentication settings, relevant when authentication-factor is set to radius.""",
    )
    secur_id: SecurIdSettingsReply = Field(
        alias="secur-id",
        description="""SecurID authentication settings, relevant when authentication-factor is set to secur-id.""",
    )
    dynamic_id: DynamicIdSettingsReply = Field(
        alias="dynamic-id",
        description="""DynamicID authentication settings, relevant when authentication-factor is set to dynamic-id.""",
    )
    identity_provider: IdentityProviderSettingsReply = Field(
        alias="identity-provider",
        description="""Identity provider authentication settings. At least one identity provider must be configured when authentication-factor is set to 'identity-provider'.""",
    )
    client_display: ClientDisplaySettingsReply = Field(
        alias="client-display",
        description="""Client display settings for this authentication method.""",
    )
