from pydantic import BaseModel, Field


class ApiOkReply(BaseModel):
    message: str = Field(alias="message", description="""Operation status.""")
