from pydantic import BaseModel, Field


class CifsAllowedDiskRequest(BaseModel):
    server_name: str = Field(
        alias="server-name",
        description="""Blocks the ability to remotely manipulate a the window's registry.""",
    )
    share_name: str = Field(alias="share-name", description="""Disk shares.""")
