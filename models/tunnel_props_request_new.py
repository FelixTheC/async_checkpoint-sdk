from pydantic import BaseModel, Field


class TunnelPropsRequestNew(BaseModel):
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
