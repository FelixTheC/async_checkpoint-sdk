from .pydantic import BaseModel, Field


class UpgradeExportReply(BaseModel):
    task_id: str = Field(
        alias="task-id",
        description="""Asynchronous task unique identifier. Use show-task command to check the progress of the task.""",
    )
    login_required: str = Field(
        alias="login-required",
        description="""If set to True, session is expired and login is required.""",
    )
