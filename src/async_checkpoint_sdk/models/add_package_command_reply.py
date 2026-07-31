from .pydantic import BaseModel, Field


class AddPackageCommandReply(BaseModel):
    task_id: str = Field(
        alias="task-id",
        description="""Unique identifier of the 'add-repository-package' task. Use the 'show-task' command to check the progress of the task.""",
    )
