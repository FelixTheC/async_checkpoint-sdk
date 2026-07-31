from pydantic import BaseModel, Field
from web_server_request_edit import WebServerRequestEdit


class HostServersRequestEdit(BaseModel):
    dns_server: bool = Field(
        alias="dns-server", description="""Gets True if this server is a DNS Server."""
    )
    mail_server: bool = Field(
        alias="mail-server", description="""Gets True if this server is a Mail Server."""
    )
    web_server: bool = Field(
        alias="web-server", description="""Gets True if this server is a Web Server."""
    )
    web_server_config: WebServerRequestEdit = Field(
        alias="web-server-config", description="""Web Server configuration."""
    )
