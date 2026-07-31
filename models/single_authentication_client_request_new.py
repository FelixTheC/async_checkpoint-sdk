from client_display_settings_request import ClientDisplaySettingsRequest
from personal_certificate_settings_request_new import (
    PersonalCertificateSettingsRequestNew,
)
from pydantic import BaseModel, Field
from radius_settings_request_new import RadiusSettingsRequestNew
from secur_id_settings_request_new import SecurIdSettingsRequestNew


class SingleAuthenticationClientRequestNew(BaseModel):
    enabled: bool = Field(
        alias="enabled",
        description="""Allow clients that support only single authentication method.""",
    )
    allow_multiple_authentication_clients: bool = Field(
        alias="allow-multiple-authentication-clients",
        description="""Allow clients that support multiple authentication methods to connect.""",
    )
    display_name: str = Field(
        alias="display-name",
        description="""Display name for the authentication method.""",
    )
    method: str = Field(alias="method", description="""Authentication method type.""")
    secur_id: SecurIdSettingsRequestNew = Field(
        alias="secur-id",
        description="""SecurID authentication settings, relevant only when method is 'secur-id'.""",
    )
    radius: RadiusSettingsRequestNew = Field(
        alias="radius",
        description="""RADIUS authentication settings, relevant only when method is 'radius'.""",
    )
    personal_certificate: PersonalCertificateSettingsRequestNew = Field(
        alias="personal-certificate",
        description="""Personal certificate authentication settings, relevant only when method is 'personal-certificate'.""",
    )
    client_display_settings: ClientDisplaySettingsRequest = Field(
        alias="client-display-settings",
        description="""Client display configuration settings.""",
    )
