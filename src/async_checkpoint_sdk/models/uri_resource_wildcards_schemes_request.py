from .pydantic import BaseModel, Field


class UriResourceWildcardsSchemesRequest(BaseModel):
    http: bool = Field(alias="http", description="""Http scheme.""")
    ftp: bool = Field(alias="ftp", description="""Ftp scheme.""")
    gopher: bool = Field(alias="gopher", description="""Gopher scheme.""")
    mailto: bool = Field(alias="mailto", description="""Mailto scheme.""")
    news: bool = Field(alias="news", description="""News scheme.""")
    wais: bool = Field(alias="wais", description="""Wais scheme.""")
    other: str = Field(
        alias="other",
        description="""You can specify another scheme in the Other field. You can use wildcards.""",
    )
