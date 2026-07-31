from pydantic import BaseModel, Field


class ImsiPrefixReply(BaseModel):
    enable: bool = Field(alias="enable", description="""""")
    prefix: str = Field(alias="prefix", description="""The IMSI prefix.""")
