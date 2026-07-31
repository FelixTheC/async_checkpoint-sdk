from .pydantic import BaseModel, Field


class HttpOptionsReply(BaseModel):
    destination: str = Field(alias="destination", description="""The destination URL.""")
