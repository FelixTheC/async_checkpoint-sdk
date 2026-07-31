from pydantic import BaseModel, Field


class DeploymentCommandReply(BaseModel):
    task_id: str = Field(
        alias="task-id",
        description="""Unique identifier of the 'install-software-package' task. Use the 'show-task' command to check the progress of the task.""",
    )
