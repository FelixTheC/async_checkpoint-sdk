from pydantic import BaseModel, Field


class RunInitInterfacesReply(BaseModel):
    message: str = Field(alias="message", description="""Operation status.""")
