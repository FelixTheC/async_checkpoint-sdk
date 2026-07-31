from .pydantic import BaseModel, Field


class DistributeLicensesReply(BaseModel):
    task_id: str = Field(
        alias="task-id",
        description="""Distribute task UID. Use show-task command to check the progress of the task.""",
    )
