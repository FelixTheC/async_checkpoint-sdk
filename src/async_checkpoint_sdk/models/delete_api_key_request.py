from pydantic import BaseModel, Field


class DeleteApiKeyRequest(BaseModel):
    api_key: str = Field(alias="api-key", description="""API key to be deleted.""")
