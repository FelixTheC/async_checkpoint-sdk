from .pydantic import BaseModel, Field


class DataCenterContentObjectFilter(BaseModel):
    text: str = Field(
        alias="text",
        description="""Return results containing the specified text value.""",
    )
    uri: str = Field(
        alias="uri",
        description="""Return results under the specified Data Center Object (identified by URI).""",
    )
