from pydantic import BaseModel, Field


class DisconnectReply(BaseModel):
    message: str = Field(alias="message", description="""Operation status.""")
