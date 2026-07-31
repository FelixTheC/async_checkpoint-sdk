from .pydantic import BaseModel, Field


class VpnCloudTunnelReply(BaseModel):
    task_id: str = Field(
        alias="task-id",
        description="""Asynchronous task unique identifier. Use show-task command to check the progress of the task.""",
    )
