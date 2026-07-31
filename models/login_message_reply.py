from pydantic import BaseModel, Field


class LoginMessageReply(BaseModel):
    header: str = Field(alias="header", description="""Message header.""")
    message: str = Field(alias="message", description="""Message content.""")
