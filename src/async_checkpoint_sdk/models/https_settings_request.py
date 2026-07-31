from pydantic import BaseModel, Field


class HttpsSettingsRequest(BaseModel):
    url: str = Field(alias="url", description="""Certificate authority URL.""")
