from pydantic import BaseModel, Field


class WorkSessionSwitchRequest(BaseModel):
    uid: str = Field(
        alias="uid",
        description="""Session unique identifier. It should belong to the current administrator. Switching to the sessions opened in SmartConsole is not supported.""",
    )
