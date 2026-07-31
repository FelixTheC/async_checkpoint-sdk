from pydantic import BaseModel, Field


class HttpServerRequest(BaseModel):
    logical_name: str = Field(
        alias="logical-name", description="""Unique Logical Name of the HTTP Server."""
    )
    host: str = Field(alias="host", description="""Host name of the HTTP Server.""")
    port: int = Field(alias="port", description="""Port number of the HTTP Server.""")
    reauthentication: str = Field(
        alias="reauthentication",
        description="""Specify whether users must reauthenticate when accessing a specific server.""",
    )
