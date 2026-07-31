from .pydantic import BaseModel, Field


class ImportSmartTaskReply(BaseModel):
    message: str = Field(alias="message", description="""Operation status.""")
