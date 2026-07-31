from .pydantic import BaseModel, Field


class WebConsoleStatisticsReply(BaseModel):
    file: str = Field(alias="file", description="""N/A""")
