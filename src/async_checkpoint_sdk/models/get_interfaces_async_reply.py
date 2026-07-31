from .pydantic import BaseModel, Field


class GetInterfacesAsyncReply(BaseModel):
    task_id: str = Field(
        alias="task-id",
        description="""The UID of the get-interfaces task. Use the show-task command to check the progress of the get-interfaces task.""",
    )
