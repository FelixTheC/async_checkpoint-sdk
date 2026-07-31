from pydantic import BaseModel, Field


class BatchReplyTask(BaseModel):
    task_id: str = Field(
        alias="task-id",
        description="""Batch task UID. Use show-task command to check the progress of the task.""",
    )
