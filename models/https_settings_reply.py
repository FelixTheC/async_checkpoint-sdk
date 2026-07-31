from pydantic import BaseModel, Field


class HttpsSettingsReply(BaseModel):
    url: str = Field(alias="url", description="""Certificate authority URL.""")
