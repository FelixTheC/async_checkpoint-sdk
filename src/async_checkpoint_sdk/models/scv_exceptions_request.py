from pydantic import BaseModel, Field


class ScvExceptionsRequest(BaseModel):
    hosts: str | list[str] = Field(
        alias="hosts", description="""Specify the Hosts to be excluded from SCV."""
    )
    services: str | list[str] = Field(
        alias="services", description="""Specify the services to be accessed."""
    )
