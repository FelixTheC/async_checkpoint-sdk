from pydantic import BaseModel, Field


class WorkSessionAssignRequest(BaseModel):
    administrator_name: str = Field(
        alias="administrator-name",
        description="""Assignee administrator name. Specify it to assign a session to another administrator.""",
    )
    uid: str = Field(
        alias="uid",
        description="""Session unique identifier. Specify it to assign a different session than the one you currently use.""",
    )
    disconnect_active_session: bool = Field(
        alias="disconnect-active-session",
        description="""Allows assignment of an active session, currently executed by another administrator.""",
    )
