from .pydantic import BaseModel, Field


class DiffReplyTask(BaseModel):
    task_id: str = Field(
        alias="task-id",
        description="""Diff task UID. Use show-task command to check the progress of the task.""",
    )
