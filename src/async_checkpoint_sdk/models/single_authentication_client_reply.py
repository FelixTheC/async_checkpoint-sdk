from .client_display_settings_reply import ClientDisplaySettingsReply
from .personal_certificate_settings_reply import PersonalCertificateSettingsReply
from .pydantic import BaseModel, Field
from .radius_settings_reply import RadiusSettingsReply
from .secur_id_settings_reply import SecurIdSettingsReply


class SingleAuthenticationClientReply(BaseModel):
    enabled: bool = Field(
        alias="enabled",
        description="""Allow clients that support only single authentication method.""",
    )
    allow_multiple_authentication_clients: bool = Field(
        alias="allow-multiple-authentication-clients",
        description="""Allow clients that support multiple authentication methods to connect.""",
    )
    display_name: str = Field(alias="display-name", description="""Display name.""")
    method: str = Field(
        alias="method",
        description="""Primary authentication method: certificate, radius, securid, username-password.""",
    )
    secur_id: SecurIdSettingsReply = Field(
        alias="secur-id",
        description="""SecurID authentication settings, relevant only when method is 'secur-id'.""",
    )
    radius: RadiusSettingsReply = Field(
        alias="radius",
        description="""RADIUS authentication settings, relevant only when method is 'radius'.""",
    )
    personal_certificate: PersonalCertificateSettingsReply = Field(
        alias="personal-certificate",
        description="""Personal certificate authentication settings, relevant only when method is 'personal-certificate'.""",
    )
    client_display_settings: ClientDisplaySettingsReply = Field(
        alias="client-display-settings", description="""client display settings."""
    )
