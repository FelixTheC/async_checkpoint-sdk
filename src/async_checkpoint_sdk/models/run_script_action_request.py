from pydantic import BaseModel, Field


class RunScriptActionRequest(BaseModel):
    repository_script: str = Field(
        alias="repository-script",
        description="""Repository script that is executed when the trigger is fired.,  identified by the name or UID.""",
    )
    targets: str | list[str] = Field(
        alias="targets", description="""Targets to execute the script on."""
    )
    time_out: int = Field(alias="time-out", description="""Script execution time-out in seconds.""")
