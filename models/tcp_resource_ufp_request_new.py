from pydantic import BaseModel, Field


class TcpResourceUfpRequestNew(BaseModel):
    caching_control: str = Field(
        alias="caching-control",
        description="""Specifies if and how caching is to be enabled.""",
    )
    ignore_ufp_server_after_failure: bool = Field(
        alias="ignore-ufp-server-after-failure",
        description="""The UFP server will be ignored after numerous UFP server connections were unsuccessful.""",
    )
    number_of_failures_before_ignore: int = Field(
        alias="number-of-failures-before-ignore",
        description="""Signifies at what point the UFP server should be ignored, Applicable only if 'ignore after fail' is enabled.""",
    )
    timeout_before_reconnecting: int = Field(
        alias="timeout-before-reconnecting",
        description="""The amount of time, in seconds, that must pass before a UFP server connection should be attempted, Applicable only if 'ignore after fail' is enabled.""",
    )
