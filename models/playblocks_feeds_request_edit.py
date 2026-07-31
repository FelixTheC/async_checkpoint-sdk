from pydantic import BaseModel, Field


class PlayblocksFeedsRequestEdit(BaseModel):
    data: str = Field(alias="data", description="""N/A""")
