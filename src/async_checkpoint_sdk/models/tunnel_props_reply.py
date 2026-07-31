from .api_object_standard_identifier import ApiObjectStandardIdentifier
from .pydantic import BaseModel, Field


class TunnelPropsReply(BaseModel):
    first_tunnel_endpoint: ApiObjectStandardIdentifier = Field(
        alias="first-tunnel-endpoint",
        description="""First tunnel endpoint (center gateway). Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    second_tunnel_endpoint: ApiObjectStandardIdentifier = Field(
        alias="second-tunnel-endpoint",
        description="""Second tunnel endpoint (center gateway for meshed VPN community and satellite gateway for star VPN community). Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
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
