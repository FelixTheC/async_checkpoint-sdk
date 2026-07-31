from pydantic import BaseModel, Field


class UriResourceCvpRequest(BaseModel):
    enable_cvp: bool = Field(
        alias="enable-cvp", description="""Select to enable the Content Vectoring Protocol."""
    )
    server: str = Field(
        alias="server",
        description="""CVP server identified by name or UID.
The CVP server must already be defined as an OPSEC Application.""",
    )
    allowed_to_modify_content: bool = Field(
        alias="allowed-to-modify-content",
        description="""Configures the CVP server to inspect but not modify content.""",
    )
    send_http_headers_to_cvp: bool = Field(
        alias="send-http-headers-to-cvp",
        description="""Select, if you would like the CVP server to check the HTTP headers of the message packets.""",
    )
    reply_order: str = Field(
        alias="reply-order",
        description="""Designates when the CVP server returns data to the Security Gateway security server.""",
    )
    send_http_request_to_cvp: bool = Field(
        alias="send-http-request-to-cvp",
        description="""Used to protect against undesirable content in the HTTP request, for example, when inspecting peer-to-peer connections.""",
    )
    send_only_unsafe_file_types: bool = Field(
        alias="send-only-unsafe-file-types",
        description="""Improves the performance of the CVP server. This option does not send to the CVP server traffic that is considered safe.""",
    )
