from .pydantic import BaseModel, Field


class ScaledIdentitySharingKeyReply(BaseModel):
    message: str = Field(alias="message", description="""Operation status.""")
