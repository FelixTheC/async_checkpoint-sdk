from .pydantic import BaseModel, Field


class PacketCaptureReply(BaseModel):
    task_id: str = Field(
        alias="task-id",
        description="""Get attachment task UID. Use show-task command to check the progress of the task.""",
    )
