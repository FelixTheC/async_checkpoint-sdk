from pydantic import BaseModel, Field


class GwProxyCmdRequest(BaseModel):
    target: str = Field(
        alias="target", description="""Gateway-object-name or gateway-ip-address or gateway-UID."""
    )
    other_parameter: str = Field(
        alias="other-parameter", description="""Other input parameters that gateway needs it."""
    )
