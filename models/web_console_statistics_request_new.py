from pydantic import BaseModel, Field


class WebConsoleStatisticsRequestNew(BaseModel):
    data: str = Field(alias="data", description="""N/A""")
    field_names: str = Field(alias="field-names", description="""N/A""")
    override_file: bool = Field(alias="override-file", description="""N/A""")
