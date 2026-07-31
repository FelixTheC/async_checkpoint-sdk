from pydantic import BaseModel, Field


class CloudApiKeyRequest(BaseModel):
    app_id: str = Field(alias="app-id", description="""N/A""")
    persist_key: bool = Field(alias="persist-key", description="""N/A""")
