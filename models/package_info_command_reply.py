from pydantic import BaseModel, Field


class PackageInfoCommandReply(BaseModel):
    task_id: str = Field(
        alias="task-id",
        description="""Unique identifier of the 'show-software-package-details' task. Use the 'show-task' command to check the progress of the task.""",
    )
