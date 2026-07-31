from .pydantic import BaseModel, Field


class InstallDbReply(BaseModel):
    tasks: list[dict] = Field(
        alias="tasks", description="""Asynchronous task unique identifiers."""
    )
