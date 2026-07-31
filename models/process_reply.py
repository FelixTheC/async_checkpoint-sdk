from pydantic import BaseModel, Field


class ProcessReply(BaseModel):
    name: str = Field(alias="name", description="""Process name.""")
    pid: str = Field(alias="pid", description="""Process id.""")
    status: str = Field(alias="status", description="""Process status.""")
