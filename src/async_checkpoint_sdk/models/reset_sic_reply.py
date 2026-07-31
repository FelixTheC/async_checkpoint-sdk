from .pydantic import BaseModel, Field


class ResetSicReply(BaseModel):
    message: str = Field(alias="message", description="""Operation status.""")
