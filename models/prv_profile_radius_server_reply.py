from pydantic import BaseModel, Field


class PrvProfileRadiusServerReply(BaseModel):
    radius_server_name: str = Field(
        alias="radius-server-name", description="""Radius server Name."""
    )
