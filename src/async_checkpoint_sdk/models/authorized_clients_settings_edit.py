from pydantic import BaseModel, Field


class AuthorizedClientsSettingsEdit(BaseModel):
    client: str = Field(alias="client", description="""Host / Network Group Name or UID.""")
    client_secret: str = Field(alias="client-secret", description="""Client Secret.""")
