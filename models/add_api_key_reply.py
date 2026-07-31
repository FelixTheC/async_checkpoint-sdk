from pydantic import BaseModel, Field


class AddApiKeyReply(BaseModel):
    api_key: str = Field(
        alias="api-key", description="""Represents the API Key to be used for Login."""
    )
