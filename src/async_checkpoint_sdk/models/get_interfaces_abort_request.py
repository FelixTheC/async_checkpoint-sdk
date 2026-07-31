from pydantic import BaseModel, Field


class GetInterfacesAbortRequest(BaseModel):
    task_id: str = Field(alias="task-id", description="""get-interfaces task UID.""")
    force_cleanup: bool = Field(
        alias="force-cleanup", description="""Forcefully abort the get-interfaces task."""
    )
