from pydantic import BaseModel, Field


class ScepSettingsRequest(BaseModel):
    ca_identifier: str = Field(
        alias="ca-identifier", description="""Certificate authority identifier."""
    )
    url: str = Field(alias="url", description="""Certificate authority URL.""")
