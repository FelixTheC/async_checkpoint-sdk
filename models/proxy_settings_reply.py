from pydantic import BaseModel, Field


class ProxySettingsReply(BaseModel):
    use_custom_proxy: bool = Field(
        alias="use-custom-proxy",
        description="""Use custom proxy settings for this network object.""",
    )
    proxy_server: str = Field(alias="proxy-server", description="""N/A""")
    port: int = Field(alias="port", description="""N/A""")
