from .pydantic import BaseModel, Field


class CommandLineReply(BaseModel):
    reply: str = Field(alias="reply", description="""N/A""")
