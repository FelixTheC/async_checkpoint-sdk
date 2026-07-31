from pydantic import BaseModel, Field


class WorkflowSubmitRequest(BaseModel):
    uid: str = Field(alias="uid", description="""Session unique identifier.""")
