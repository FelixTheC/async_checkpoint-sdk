from api_object_standard_identifier import ApiObjectStandardIdentifier
from pydantic import BaseModel, Field


class TcpResourceCvpReply(BaseModel):
    server: ApiObjectStandardIdentifier = Field(
        alias="server",
        description="""The CVP server defined as an OPSEC Application.""",
    )
    cvp_server_is_allowed_to_modify_content: bool = Field(
        alias="cvp-server-is-allowed-to-modify-content",
        description="""Configures the CVP server to inspect but not modify content.""",
    )
    reply_order: str = Field(
        alias="reply-order",
        description="""Designates when the CVP server returns data to the Security Gateway security server.""",
    )
