from pydantic import BaseModel, Field


class TunnelPropsRequestRemove(BaseModel):
    first_tunnel_endpoint: str = Field(
        alias="first-tunnel-endpoint",
        description="""First tunnel endpoint (center gateway).
Identified by name or UID.""",
    )
    second_tunnel_endpoint: str = Field(
        alias="second-tunnel-endpoint",
        description="""Second tunnel endpoint (center gateway for meshed VPN community and satellitegateway for star VPN community). 
Identified by name or UID.""",
    )
