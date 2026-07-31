from authentication_settings_idc_reply import AuthenticationSettingsIdcReply
from i_d_a_portal_reply import IDAPortalReply
from pydantic import BaseModel, Field


class IdentityCollectorSettingsReply(BaseModel):
    authentication_settings: AuthenticationSettingsIdcReply = Field(
        alias="authentication-settings",
        description="""Authentication Settings for Identity Collector.""",
    )
    authorized_clients: list[dict] = Field(
        alias="authorized-clients", description="""Authorized Clients."""
    )
    client_access_permissions: IDAPortalReply = Field(
        alias="client-access-permissions",
        description="""Identity Collector accessibility settings.""",
    )
