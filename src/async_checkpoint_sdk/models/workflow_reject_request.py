from pydantic import BaseModel, Field


class WorkflowRejectRequest(BaseModel):
    uid: str = Field(alias="uid", description="""Session unique identifier.""")
    comments: str = Field(alias="comments", description="""Reject justification.""")
