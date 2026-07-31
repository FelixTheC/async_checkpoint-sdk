from .add import add
from .gw_props_request_new import GwPropsRequestNew
from .pydantic import BaseModel, Field
from .remove import remove
from .star_rim_request import StarRimRequest
from .tunnel_props_request import TunnelPropsRequest
from .update import update


class StarPermanentTunnelsRequestEdit(BaseModel):
    set_permanent_tunnels: str = Field(
        alias="set-permanent-tunnels",
        description="""Indicates which tunnels to set as permanent.""",
    )
    gateways: add | remove | update | GwPropsRequestNew | list[dict] = Field(
        alias="gateways",
        description="""List of gateways to set all their tunnels to permanent with specified track options. Will take effect only if set-permanent-tunnels-on is set to all-tunnels-of-specific-gateways.""",
    )
    tunnels: add | remove | update | TunnelPropsRequest | list[dict] = Field(
        alias="tunnels",
        description="""List of tunnels to set as permanent with specified track options. Will take effect only if set-permanent-tunnels-on is set to specific-tunnels-in-the-community.""",
    )
    rim: StarRimRequest = Field(alias="rim", description="""Route Injection Mechanism settings.""")
    tunnel_down_track: str = Field(
        alias="tunnel-down-track",
        description="""VPN community permanent tunnels down track option.""",
    )
    tunnel_up_track: str = Field(
        alias="tunnel-up-track", description="""Permanent tunnels up track option."""
    )
