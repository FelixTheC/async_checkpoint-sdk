from pydantic import BaseModel, Field


class WorkSessionTakeOverRequest(BaseModel):
    uid: str = Field(alias="uid", description="""Session unique identifier.""")
    disconnect_active_session: bool = Field(
        alias="disconnect-active-session",
        description="""Allows taking over of an active session, currently executed by another administrator.""",
    )
