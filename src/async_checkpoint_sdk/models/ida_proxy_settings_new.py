from pydantic import BaseModel, Field


class IdaProxySettingsNew(BaseModel):
    detect_using_x_forward_for: bool = Field(
        alias="detect-using-x-forward-for",
        description="""Whether to use X-Forward-For HTTP header, which is added by the proxy server to keep track of the original source IP.""",
    )
