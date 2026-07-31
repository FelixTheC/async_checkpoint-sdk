from .pydantic import BaseModel, Field


class UriResourceConnectionMethodsRequest(BaseModel):
    transparent: bool = Field(
        alias="transparent",
        description="""The security server is invisible to the client that originates the connection, and to the server. The Transparent connection method is the most secure.""",
    )
    proxy: bool = Field(
        alias="proxy",
        description="""The Resource is applied when people specify the Check Point Security Gateway as a proxy in their browser.""",
    )
    tunneling: bool = Field(
        alias="tunneling",
        description="""The Resource is applied when people specify the Security Gateway as a proxy in their browser, and is used for connections where Security Gateway cannot examine the contents of the packets, not even the URL.""",
    )
