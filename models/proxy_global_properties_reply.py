from pydantic import BaseModel, Field


class ProxyGlobalPropertiesReply(BaseModel):
    use_proxy_server: bool = Field(
        alias="use-proxy-server",
        description="""If set to true, a proxy server is used when features need to access the internet.""",
    )
    proxy_address: str = Field(
        alias="proxy-address",
        description="""Specify the URL or IP address of the proxy server.<br>Available only if use-proxy-server is set to true.""",
    )
    proxy_port: int = Field(
        alias="proxy-port",
        description="""Specify the Port on which the server will be accessed.<br>Available only if use-proxy-server is set to true.""",
    )
