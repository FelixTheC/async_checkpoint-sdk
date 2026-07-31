from .pydantic import BaseModel, Field


class RunScriptActionRequest(BaseModel):
    targets: str | list[str] = Field(
        alias="targets", description="""Targets to execute the script on."""
    )
    time_out: int = Field(alias="time-out", description="""Script execution time-out in seconds.""")
