from add import add
from http_server_request import HttpServerRequest
from pydantic import BaseModel, Field
from remove import remove


class SecurityServerGlobalPropertiesRequest(BaseModel):
    client_auth_welcome_file: str = Field(
        alias="client-auth-welcome-file",
        description="""Client authentication welcome file is the name of a file whose contents are to be displayed when a user begins a Client Authenticated session (optional) using the Manual Sign On Method. Client Authenticated Sessions initiated by Manual Sign On are not mediated by a security server.""",
    )
    ftp_welcome_msg_file: str = Field(
        alias="ftp-welcome-msg-file",
        description="""FTP welcome message file is the name of a file whose contents are to be displayed when a user begins an Authenticated FTP session.""",
    )
    rlogin_welcome_msg_file: str = Field(
        alias="rlogin-welcome-msg-file",
        description="""Rlogin welcome message file is the name of a file whose contents are to be displayed when a user begins an Authenticated RLOGIN session.""",
    )
    telnet_welcome_msg_file: str = Field(
        alias="telnet-welcome-msg-file",
        description="""Telnet welcome message file is the name of a file whose contents are to be displayed when a user begins an Authenticated Telnet session.""",
    )
    mdq_welcome_msg: str = Field(
        alias="mdq-welcome-msg",
        description="""MDQ Welcome Message is the message to be displayed when a user begins an MDQ session. The MDQ Welcome Message should contain characters according to RFC 1035 and it must follow the ARPANET host name rules:<br>   - This message must begin with a number or letter. After the first letter or number character the remaining characters can be a letter, number, space, tab or hyphen.<br>   - This message must not end with a space or a tab and is limited to 63 characters.""",
    )
    smtp_welcome_msg: str = Field(
        alias="smtp-welcome-msg",
        description="""SMTP Welcome Message is the message to be displayed when a user begins an SMTP session.""",
    )
    http_servers: add | remove | HttpServerRequest | list[dict] = Field(
        alias="http-servers",
        description="""This list specifies the HTTP servers. Defining HTTP servers allows you to restrict incoming HTTP.""",
    )
    server_for_null_requests: str = Field(
        alias="server-for-null-requests",
        description="""The Logical Name of a Null Requests Server from http-servers.""",
    )
