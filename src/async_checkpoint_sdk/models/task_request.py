from pydantic import BaseModel, Field


class TaskRequest(BaseModel):
    task_id: str | list[str] = Field(
        alias="task-id", description="""Unique identifier of one or more tasks."""
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
