from .pydantic import BaseModel, Field


class AuthorizedClientsSettingsReply(BaseModel):
    client: str = Field(alias="client", description="""Client Name or UID.""")
