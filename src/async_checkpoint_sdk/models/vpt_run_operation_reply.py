from .pydantic import BaseModel, Field


class VptRunOperationReply(BaseModel):
    task_id: str = Field(
        alias="task-id",
        description="""Operation task UID. Use the <i>show-task</i> command to check the progress of the task.""",
    )
