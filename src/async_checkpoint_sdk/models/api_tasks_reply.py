from .pydantic import BaseModel, Field


class ApiTasksReply(BaseModel):
    tasks: list[str] = Field(alias="tasks", description="""Asynchronous task unique identifiers.""")
