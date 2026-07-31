from .pydantic import BaseModel, Field


class HttpServerRequest(BaseModel):
    port: int = Field(alias="port", description="""Port number of the HTTP Server.""")
    reauthentication: str = Field(
        alias="reauthentication",
        description="""Specify whether users must reauthenticate when accessing a specific server.""",
    )
