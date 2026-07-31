from .pydantic import BaseModel, Field


class SslNetworkExtenderReply(BaseModel):
    ssl_enable: bool = Field(
        alias="ssl-enable", description="""Enables SSL on the Interoperable Device."""
    )
