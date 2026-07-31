from .authentication_settings_idc_new import AuthenticationSettingsIdcNew
from .identity_collector_portal_api_request import IdentityCollectorPortalApiRequest
from .pydantic import BaseModel, Field


class IdentityCollectorSettingsNew(BaseModel):
    authentication_settings: AuthenticationSettingsIdcNew = Field(
        alias="authentication-settings",
        description="""Authentication Settings for Identity Collector.""",
    )
    client_access_permissions: IdentityCollectorPortalApiRequest = Field(
        alias="client-access-permissions",
        description="""Identity Collector accessibility settings.""",
    )
