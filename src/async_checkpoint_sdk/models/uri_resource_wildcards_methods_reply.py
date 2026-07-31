from .pydantic import BaseModel, Field


class UriResourceWildcardsMethodsReply(BaseModel):
    get: bool = Field(alias="get", description="""GET method.""")
    post: bool = Field(alias="post", description="""POST method.""")
    head: bool = Field(alias="head", description="""HEAD method.""")
    put: bool = Field(alias="put", description="""PUT method.""")
    other: str = Field(
        alias="other",
        description="""You can specify another method in the Other field. You can use wildcards.""",
    )
