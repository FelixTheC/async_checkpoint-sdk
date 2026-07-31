from pydantic import BaseModel, Field


class PackagesInfoCommandReply(BaseModel):
    task_id: str = Field(
        alias="task-id",
        description="""Unique identifier of the 'show-repository-packages' task. Use the 'show-task' command to check the progress of the task.""",
    )
