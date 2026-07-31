from .pydantic import BaseModel, Field


class AutoCompleteReply(BaseModel):
    data: list[dict] = Field(alias="data", description="""N/A""")
