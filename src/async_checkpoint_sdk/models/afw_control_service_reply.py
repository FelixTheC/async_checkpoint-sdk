from pydantic import BaseModel, Field


class AfwControlServiceReply(BaseModel):
    message: str = Field(alias="message", description="""TBD.""")
    status: str = Field(alias="status", description="""TBD.""")
