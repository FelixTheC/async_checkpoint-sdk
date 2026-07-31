from .object import Object
from .pydantic import BaseModel, Field


class GwProxyCmdReply(BaseModel):
    command_name: str = Field(alias="command-name", description="""Target's api command.""")
    response_message: Object = Field(
        alias="response-message",
        description="""Response's object from .the target in json format.""",
    )
