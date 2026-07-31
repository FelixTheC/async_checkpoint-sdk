from pydantic import BaseModel, Field


class SendWebRequestActionRequest(BaseModel):
    fingerprint: str = Field(
        alias="fingerprint",
        description="""The SHA1 fingerprint of the URL's SSL certificate. Used to trust servers with self-signed SSL certificates.""",
    )
    override_proxy: bool = Field(
        alias="override-proxy",
        description="""Option to send to the web request via a proxy other than the Management's Server proxy (if defined).""",
    )
    proxy_url: str = Field(
        alias="proxy-url", description="""URL of the proxy used to send the request."""
    )
    shared_secret: str = Field(
        alias="shared-secret",
        description="""Shared secret that can be used by the target server to identify the Management Server.<br>The value will be sent as part of the request in the X-chkp-shared-secret header.""",
    )
    time_out: int = Field(
        alias="time-out", description="""Web Request time-out in seconds."""
    )
