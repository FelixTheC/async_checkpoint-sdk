from .pydantic import BaseModel, Field


class CifsAllowedDiskReply(BaseModel):
    server_name: str = Field(alias="server-name", description="""Logs each share map attempt.""")
    share_name: str = Field(alias="share-name", description="""Logs each share map attempt.""")
