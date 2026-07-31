from .pydantic import BaseModel, Field


class WireModeReply(BaseModel):
    allow_uninspected_encrypted_traffic: bool = Field(
        alias="allow-uninspected-encrypted-traffic",
        description="""Allow uninspected encrypted traffic between Wire mode interfaces of this Community members.""",
    )
    allow_uninspected_encrypted_routing: bool = Field(
        alias="allow-uninspected-encrypted-routing",
        description="""Allow members to route uninspected encrypted traffic in VPN routing configurations.""",
    )
