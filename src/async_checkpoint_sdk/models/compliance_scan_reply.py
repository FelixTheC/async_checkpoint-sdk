from .pydantic import BaseModel, Field


class ComplianceScanReply(BaseModel):
    task_id: str = Field(
        alias="task-id",
        description="""Compliance scan task UID. Use the show-task command to check the progress of the task.""",
    )
