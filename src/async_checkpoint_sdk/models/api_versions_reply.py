from pydantic import BaseModel, Field


class ApiVersionsReply(BaseModel):
    current_version: str = Field(alias="current-version", description="""N/A""")
    supported_versions: list[str] = Field(alias="supported-versions", description="""N/A""")
