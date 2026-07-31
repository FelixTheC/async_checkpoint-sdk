from add import add
from authentication_settings_idc_edit import AuthenticationSettingsIdcEdit
from authorized_clients_settings_edit import AuthorizedClientsSettingsEdit
from identity_collector_portal_api_request import IdentityCollectorPortalApiRequest
from pydantic import BaseModel, Field
from remove import remove


class IdentityCollectorSettingsEdit(BaseModel):
    authentication_settings: AuthenticationSettingsIdcEdit = Field(
        alias="authentication-settings",
        description="""Authentication Settings for Identity Collector.""",
    )
    authorized_clients: add | remove | AuthorizedClientsSettingsEdit | list[dict] = (
        Field(alias="authorized-clients", description="""Authorized Clients.""")
    )
    client_access_permissions: IdentityCollectorPortalApiRequest = Field(
        alias="client-access-permissions",
        description="""Identity Collector accessibility settings.""",
    )
