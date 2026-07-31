from pydantic import BaseModel, Field


class PublishReply(BaseModel):
    task_id: str = Field(
        alias="task-id",
        description="""Publish task UID. Use show-task command to check the progress of the task.""",
    )
