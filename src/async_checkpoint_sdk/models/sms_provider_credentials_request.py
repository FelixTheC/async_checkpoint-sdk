from pydantic import BaseModel, Field


class SmsProviderCredentialsRequest(BaseModel):
    username: str = Field(alias="username", description="""SMS provider username.""")
    password: str = Field(alias="password", description="""SMS provider password.""")
    api_id: str = Field(alias="api-id", description="""SMS provider API ID.""")
