from authentication_settings_web_api_reply import AuthenticationSettingsWebApiReply
from i_d_a_portal_reply import IDAPortalReply
from pydantic import BaseModel, Field


class IdentityWebApiSettingsReply(BaseModel):
    authentication_settings: AuthenticationSettingsWebApiReply = Field(
        alias="authentication-settings",
        description="""Authentication Settings for Identity Web Api.""",
    )
    authorized_clients: list[dict] = Field(
        alias="authorized-clients", description="""Authorized Clients."""
    )
    client_access_permissions: IDAPortalReply = Field(
        alias="client-access-permissions",
        description="""Identity Web Api accessibility settings.""",
    )
