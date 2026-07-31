from pydantic import BaseModel, Field


class AzureADTaskReply(BaseModel):
    task_id: str = Field(
        alias="task-id",
        description="""Azure AD Operation task-id, use show-task command to check the progress of the task.""",
    )
