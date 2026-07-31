from .pydantic import BaseModel, Field


class ScvExceptionsReply(BaseModel):
    hosts: list[dict] = Field(
        alias="hosts", description="""Specify the Hosts to be excluded from .SCV."""
    )
    services: list[dict] = Field(
        alias="services", description="""Specify the services to be accessed."""
    )
