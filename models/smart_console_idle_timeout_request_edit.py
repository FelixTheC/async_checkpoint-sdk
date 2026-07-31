from pydantic import BaseModel, Field


class SmartConsoleIdleTimeoutRequestEdit(BaseModel):
    enabled: bool = Field(
        alias="enabled",
        description="""Indicates whether to perform logout after being idle.""",
    )
    timeout_duration: int = Field(
        alias="timeout-duration",
        description="""Number of minutes that the SmartConsole will automatically logout after being idle.<br>Updating the interval will take effect only on the next login.""",
    )
