from .pydantic import BaseModel, Field


class ShowCommandsReply(BaseModel):
    commands: list[dict] = Field(alias="commands", description="""List of commands.""")
