from pydantic import BaseModel, Field


class ClusterAsyncReply(BaseModel):
    task_id: str = Field(
        alias="task-id",
        description="""Task UID. Use show-task command to check the progress of the task.""",
    )
