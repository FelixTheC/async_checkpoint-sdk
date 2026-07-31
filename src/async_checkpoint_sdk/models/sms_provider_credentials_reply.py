from .pydantic import BaseModel, Field


class SmsProviderCredentialsReply(BaseModel):
    username: str = Field(alias="username", description="""SMS provider username.""")
    api_id: str = Field(alias="api-id", description="""SMS provider API ID.""")
