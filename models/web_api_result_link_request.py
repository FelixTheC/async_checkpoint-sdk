from pydantic import BaseModel, Field


class WebApiResultLinkRequest(BaseModel):
    task_id: str = Field(alias="task-id", description="""N/A""")
