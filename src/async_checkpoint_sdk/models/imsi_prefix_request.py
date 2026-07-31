from .pydantic import BaseModel, Field


class ImsiPrefixRequest(BaseModel):
    enable: bool = Field(alias="enable", description="""""")
    prefix: str = Field(alias="prefix", description="""The IMSI prefix.""")
