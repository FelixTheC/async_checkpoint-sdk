from pydantic import BaseModel, Field


class WebApiLogoutReply(BaseModel):
    message: str = Field(alias="message", description="""Operation status.""")
