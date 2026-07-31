from .pydantic import BaseModel, Field


class LsmBaseCommandReply(BaseModel):
    tasks: list[dict] = Field(
        alias="tasks", description="""Asynchronous task unique identifiers."""
    )
