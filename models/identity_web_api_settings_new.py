from authentication_settings_web_api_new import AuthenticationSettingsWebApiNew
from identity_web_api_portal_api_request import IdentityWebApiPortalApiRequest
from pydantic import BaseModel, Field


class IdentityWebApiSettingsNew(BaseModel):
    authentication_settings: AuthenticationSettingsWebApiNew = Field(
        alias="authentication-settings",
        description="""Authentication Settings for Identity Web Api.""",
    )
    client_access_permissions: IdentityWebApiPortalApiRequest = Field(
        alias="client-access-permissions",
        description="""Identity Web Api accessibility settings.""",
    )
