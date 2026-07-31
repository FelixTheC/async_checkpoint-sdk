from pydantic import BaseModel, Field


class TcpResourceCvpRequestEdit(BaseModel):
    server: str = Field(
        alias="server",
        description="""CVP server identified by name or UID.
The CVP server must already be defined as an OPSEC Application.""",
    )
    allowed_to_modify_content: bool = Field(
        alias="allowed-to-modify-content",
        description="""Configures the CVP server to inspect but not modify content.""",
    )
    reply_order: str = Field(
        alias="reply-order",
        description="""Designates when the CVP server returns data to the Security Gateway security server.""",
    )
