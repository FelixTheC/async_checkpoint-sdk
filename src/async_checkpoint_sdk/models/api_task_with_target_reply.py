from .pydantic import BaseModel, Field


class ApiTaskWithTargetReply(BaseModel):
    target: str = Field(alias="target", description="""The target object name.""")
    task_id: str = Field(
        alias="task-id",
        description="""Asynchronous task unique identifier. Use show-task command to check the progress of the task.""",
    )
