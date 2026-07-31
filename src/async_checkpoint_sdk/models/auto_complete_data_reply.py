from .pydantic import BaseModel, Field


class AutoCompleteDataReply(BaseModel):
    description: str = Field(alias="description", description="""N/A""")
    name: str = Field(alias="name", description="""N/A""")
