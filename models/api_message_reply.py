from pydantic import BaseModel, Field


class ApiMessageReply(BaseModel):
    message: str = Field(alias="message", description="""Operation status.""")
