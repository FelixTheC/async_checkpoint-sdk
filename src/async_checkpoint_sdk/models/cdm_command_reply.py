from .pydantic import BaseModel, Field


class CdmCommandReply(BaseModel):
    tasks: list[str] = Field(alias="tasks", description="""Asynchronous task unique identifiers.""")
