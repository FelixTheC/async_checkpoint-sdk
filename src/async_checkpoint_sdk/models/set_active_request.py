from .pydantic import BaseModel, Field


class SetActiveRequest(BaseModel):
    force: bool = Field(alias="force", description="""N/A""")
