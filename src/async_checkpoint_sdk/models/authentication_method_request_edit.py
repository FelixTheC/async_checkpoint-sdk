from client_display_settings_request import ClientDisplaySettingsRequest
from dynamic_id_settings_request import DynamicIdSettingsRequest
from identity_provider_settings_request import IdentityProviderSettingsRequest
from personal_certificate_settings_request import PersonalCertificateSettingsRequest
from pydantic import BaseModel, Field
from radius_settings_request import RadiusSettingsRequest
from secur_id_settings_request import SecurIdSettingsRequest


class AuthenticationMethodRequestEdit(BaseModel):
    authentication_factor: str = Field(
        alias="authentication-factor",
        description="""Type of authentication factor. 'personal-certificate' can only be used as a first authentication method. 'dynamic-id' cannot be used as a first authentication method. Only one authentication method can be added per authentication factor type.""",
    )
    position: int = Field(
        alias="position",
        description="""Position in the authentication methods list (1-based). This field is only relevant for SET commands with ADD action. Determines the order in which authentication methods are tried. If not provided, the method will be appended to the end of the list. This field is not supported in ADD command and will be rejected if provided.""",
    )
    personal_certificate: PersonalCertificateSettingsRequest = Field(
        alias="personal-certificate",
        description="""Personal certificate authentication settings, relevant when authentication-factor is set to personal-certificate.""",
    )
    radius: RadiusSettingsRequest = Field(
        alias="radius",
        description="""RADIUS authentication settings, relevant when authentication-factor is set to radius.""",
    )
    secur_id: SecurIdSettingsRequest = Field(
        alias="secur-id",
        description="""SecurID authentication settings, relevant when authentication-factor is set to secur-id.""",
    )
    dynamic_id: DynamicIdSettingsRequest = Field(
        alias="dynamic-id",
        description="""Dynamic ID authentication settings, relevant when authentication-factor is set to dynamic-id.""",
    )
    identity_provider: IdentityProviderSettingsRequest = Field(
        alias="identity-provider",
        description="""Identity provider authentication settings. At least one identity provider must be configured when authentication-factor is set to 'identity-provider'.""",
    )
    client_display: ClientDisplaySettingsRequest = Field(
        alias="client-display",
        description="""Client display settings for this authentication method.""",
    )
