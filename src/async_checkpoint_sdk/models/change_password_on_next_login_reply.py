from pydantic import BaseModel, Field


class ChangePasswordOnNextLoginReply(BaseModel):
    message: str = Field(alias="message", description="""Operation status.""")
