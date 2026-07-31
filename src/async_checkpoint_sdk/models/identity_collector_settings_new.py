from authentication_settings_idc_new import AuthenticationSettingsIdcNew
from authorized_clients_settings_new import AuthorizedClientsSettingsNew
from identity_collector_portal_api_request import IdentityCollectorPortalApiRequest
from pydantic import BaseModel, Field


class IdentityCollectorSettingsNew(BaseModel):
    authorized_clients: AuthorizedClientsSettingsNew | list[dict] = Field(
        alias="authorized-clients", description="""Authorized Clients."""
    )
    authentication_settings: AuthenticationSettingsIdcNew = Field(
        alias="authentication-settings",
        description="""Authentication Settings for Identity Collector.""",
    )
    client_access_permissions: IdentityCollectorPortalApiRequest = Field(
        alias="client-access-permissions",
        description="""Identity Collector accessibility settings.""",
    )
