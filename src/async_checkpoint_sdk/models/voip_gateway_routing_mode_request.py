from .pydantic import BaseModel, Field


class VoipGatewayRoutingModeRequest(BaseModel):
    call_setup: bool = Field(
        alias="call-setup",
        description="""Indicates whether the routing mode includes call setup (Q.931).""",
    )
    call_setup_and_call_control: bool = Field(
        alias="call-setup-and-call-control",
        description="""Indicates whether the routing mode includes both call setup (Q.931) and call control (H.245).""",
    )
