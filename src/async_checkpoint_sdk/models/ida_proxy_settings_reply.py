from .pydantic import BaseModel, Field


class IdaProxySettingsReply(BaseModel):
    detect_using_x_forward_for: bool = Field(
        alias="detect-using-x-forward-for",
        description="""Whether X-Forward-For HTTP header is been used.""",
    )
