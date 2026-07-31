from .pydantic import BaseModel, Field


class DeleteObjectsByTagRequest(BaseModel):
    async_response: bool = Field(
        alias="async-response",
        description="""Run command in asynchronous mode and return task UID. Use show-task command to check the progress of the task.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
