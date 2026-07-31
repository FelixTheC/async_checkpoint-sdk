from pydantic import BaseModel, Field


class MdsStatReply(BaseModel):
    servers: list[dict] = Field(alias="servers", description="""Servers status.""")
