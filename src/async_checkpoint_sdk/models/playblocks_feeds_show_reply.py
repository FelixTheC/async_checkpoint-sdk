from pydantic import BaseModel, Field


class PlayblocksFeedsShowReply(BaseModel):
    data: str = Field(alias="data", description="""N/A""")
    filepath: str = Field(alias="filePath", description="""N/A""")
