from .pydantic import BaseModel, Field


class TaskReply(BaseModel):
    tasks: list[dict] = Field(alias="tasks", description="""N/A""")
