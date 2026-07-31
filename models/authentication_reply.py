from dynamic_id_settings_reply import DynamicIdSettingsReply
from pydantic import BaseModel, Field
from single_authentication_client_reply import SingleAuthenticationClientReply


class AuthenticationReply(BaseModel):
    single_authentication_client: SingleAuthenticationClientReply = Field(
        alias="single-authentication-client",
        description="""Settings for clients that support only single authentication method.""",
    )
    authentication_clients: list[dict] = Field(
        alias="authentication-clients",
        description="""Collection of VPN Authentication clients identified by the name or UID.""",
    )
    override_global_dynamic_id_settings: bool = Field(
        alias="override-global-dynamic-id-settings",
        description="""Override global dynamic ID settings.""",
    )
    dynamic_id_settings: DynamicIdSettingsReply = Field(
        alias="dynamic-id-settings",
        description="""Dynamic ID settings, relevant only when override-global-dynamic-id-settings is true.""",
    )
    send_machine_certificate: str = Field(
        alias="send-machine-certificate",
        description="""Configure when to send machine certificate.""",
    )
