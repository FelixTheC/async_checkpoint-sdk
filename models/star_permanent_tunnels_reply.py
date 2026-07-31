from pydantic import BaseModel, Field
from star_rim_reply import StarRimReply


class StarPermanentTunnelsReply(BaseModel):
    set_permanent_tunnels: str = Field(
        alias="set-permanent-tunnels",
        description="""Indicates which tunnels to set as permanent.""",
    )
    gateways: list[dict] = Field(
        alias="gateways",
        description="""List of gateways to set all their tunnels to permanent with specified track options.""",
    )
    tunnels: list[dict] = Field(
        alias="tunnels",
        description="""List of tunnels to set as permanent with specified track options.""",
    )
    rim: StarRimReply = Field(
        alias="rim", description="""Route Injection Mechanism settings."""
    )
    tunnel_down_track: str = Field(
        alias="tunnel-down-track", description="""Permanent tunnel down track method."""
    )
    tunnel_up_track: str = Field(
        alias="tunnel-up-track",
        description="""VPN community permanent tunnels down track option.""",
    )
