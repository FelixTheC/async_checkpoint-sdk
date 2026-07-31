from .pydantic import BaseModel, Field


class VerifyPolicyReply(BaseModel):
    task_id: str = Field(
        alias="task-id",
        description="""Verify task UID. Use show-task command to check the progress of the task.""",
    )
