from pydantic import BaseModel, Field


class ShowCommandReply(BaseModel):
    description: str = Field(alias="description", description="""Command Description.""")
    name: str = Field(alias="name", description="""Command Name.""")
