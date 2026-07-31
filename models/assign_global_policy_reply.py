from pydantic import BaseModel, Field


class AssignGlobalPolicyReply(BaseModel):
    tasks: list[str] = Field(
        alias="tasks", description="""Asynchronous task unique identifiers."""
    )
