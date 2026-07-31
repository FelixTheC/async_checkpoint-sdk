from pydantic import BaseModel, Field


class TunnelPropsRequestNew(BaseModel):
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
    track_options: str = Field(
        alias="track-options",
        description="""Indicates whether to use the community track options or to override track options for the permanent tunnels.""",
    )
    override_tunnel_down_track: str = Field(
        alias="override-tunnel-down-track",
        description="""Gateway tunnel down track option. Relevant only if the track-options is set to 'override track options'.""",
    )
    override_tunnel_up_track: str = Field(
        alias="override-tunnel-up-track",
        description="""Gateway tunnel up track option. Relevant only if the track-options is set to 'override track options'.""",
    )
