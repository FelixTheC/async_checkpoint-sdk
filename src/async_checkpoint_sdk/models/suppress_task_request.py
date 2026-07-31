from pydantic import BaseModel, Field


class SuppressTaskRequest(BaseModel):
    all_completed_tasks: bool = Field(
        alias="all-completed-tasks",
        description="""Suppress all the tasks that are not in progress.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Ignore warnings if exist."""
    )
