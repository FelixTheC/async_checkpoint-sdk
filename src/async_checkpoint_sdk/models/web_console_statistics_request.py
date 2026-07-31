from pydantic import BaseModel, Field


class WebConsoleStatisticsRequest(BaseModel):
    file_name: str = Field(alias="file-name", description="""N/A""")
