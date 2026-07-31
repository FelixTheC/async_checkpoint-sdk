from .pydantic import BaseModel, Field


class WebApiExportRequest(BaseModel):
    exclude_classes: list[str] = Field(alias="exclude-classes", description="""N/A""")
    exclude_topics: list[str] = Field(alias="exclude-topics", description="""N/A""")
    export_files_by_class: bool = Field(alias="export-files-by-class", description="""N/A""")
    include_classes: list[str] = Field(alias="include-classes", description="""N/A""")
    include_topics: list[str] = Field(alias="include-topics", description="""N/A""")
    query_limit: int = Field(alias="query-limit", description="""N/A""")
