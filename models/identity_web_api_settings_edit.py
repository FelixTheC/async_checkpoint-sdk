from add import add
from authentication_settings_web_api_edit import AuthenticationSettingsWebApiEdit
from authorized_clients_settings_edit import AuthorizedClientsSettingsEdit
from identity_web_api_portal_api_request import IdentityWebApiPortalApiRequest
from pydantic import BaseModel, Field
from remove import remove


class IdentityWebApiSettingsEdit(BaseModel):
    authentication_settings: AuthenticationSettingsWebApiEdit = Field(
        alias="authentication-settings",
        description="""Authentication Settings for Identity Web Api.""",
    )
    authorized_clients: add | remove | AuthorizedClientsSettingsEdit | list[dict] = (
        Field(alias="authorized-clients", description="""Authorized Clients.""")
    )
    client_access_permissions: IdentityWebApiPortalApiRequest = Field(
        alias="client-access-permissions",
        description="""Identity Web Api accessibility settings.""",
    )
