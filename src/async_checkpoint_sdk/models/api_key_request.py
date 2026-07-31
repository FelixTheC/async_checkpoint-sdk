from pydantic import BaseModel, Field


class ApiKeyRequest(BaseModel):
    admin_uid: str = Field(
        alias="admin-uid", description="""Administrator uid to generate API key for."""
    )
