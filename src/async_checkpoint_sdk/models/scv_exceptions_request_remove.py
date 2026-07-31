from pydantic import BaseModel, Field


class ScvExceptionsRequestRemove(BaseModel):
    hosts: str | list[str] = Field(
        alias="hosts", description="""Specify the Hosts to be excluded from SCV."""
    )
