from pydantic import BaseModel, Field


class WorkflowApproveRequest(BaseModel):
    uid: str = Field(alias="uid", description="""Session unique identifier.""")
