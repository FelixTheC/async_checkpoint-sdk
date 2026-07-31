from gw_props_request_new import GwPropsRequestNew
from meshed_rim_request_new import MeshedRimRequestNew
from pydantic import BaseModel, Field
from tunnel_props_request_new import TunnelPropsRequestNew


class MeshedPermanentTunnelsRequestNew(BaseModel):
    set_permanent_tunnels: str = Field(
        alias="set-permanent-tunnels",
        description="""Indicates which tunnels to set as permanent.""",
    )
    gateways: GwPropsRequestNew | list[dict] = Field(
        alias="gateways",
        description="""List of gateways to set all their tunnels to permanent with specified track options. Will take effect only if set-permanent-tunnels-on is set to all-tunnels-of-specific-gateways.""",
    )
    tunnels: TunnelPropsRequestNew | list[dict] = Field(
        alias="tunnels",
        description="""List of tunnels to set as permanent with specified track options. Will take effect only if set-permanent-tunnels-on is set to specific-tunnels-in-the-community.""",
    )
    rim: MeshedRimRequestNew = Field(
        alias="rim", description="""Route Injection Mechanism settings."""
    )
    tunnel_down_track: str = Field(
        alias="tunnel-down-track",
        description="""VPN community permanent tunnels down track option.""",
    )
    tunnel_up_track: str = Field(
        alias="tunnel-up-track", description="""Permanent tunnels up track option."""
    )
