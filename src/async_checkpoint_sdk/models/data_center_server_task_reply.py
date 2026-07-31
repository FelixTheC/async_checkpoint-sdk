from .pydantic import BaseModel, Field


class DataCenterServerTaskReply(BaseModel):
    task_id: str = Field(
        alias="task-id",
        description="""Data Center Operation task-id, use show-task command to check the progress of the task.""",
    )
