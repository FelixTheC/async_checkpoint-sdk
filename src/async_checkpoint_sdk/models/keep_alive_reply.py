from .pydantic import BaseModel, Field


class KeepAliveReply(BaseModel):
    message: str = Field(alias="message", description="""Operation status.""")
