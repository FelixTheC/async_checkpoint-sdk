from .object import Object
from .pydantic import BaseModel, Field


class VpnAdvancedRequest(BaseModel):
    tunnel_sharing_mode: str = Field(
        alias="tunnel-sharing-mode",
        description="""VPN tunnel sharing mode: 'use-community' (follow community settings), 'custom-host-pair' (one tunnel per host pair), 'custom-subnet-pair' (one tunnel per subnet pair - IPSec standard), 'custom-gateway-pair' (one tunnel per gateway pair).""",
    )
    shutdown_on_gateway_restart: bool = Field(
        alias="shutdown-on-gateway-restart",
        description="""Enable restart options for Remote Access clients. Gateway saves tunnel details and sends Delete SA message after restart to reinitiate tunnels.""",
    )
    enable_wire_mode: bool = Field(
        alias="enable-wire-mode",
        description="""Enable Wire Mode to improve connectivity by bypassing firewall enforcement for VPN traffic, treating internal interfaces as trusted.""",
    )
    wire_mode_interfaces: Object = Field(
        alias="wire-mode-interfaces",
        description="""Collection of interface names or UIDs to include in Wire Mode. Supports add/remove operations.""",
    )
    enable_wire_mode_log_traffic: bool = Field(
        alias="enable-wire-mode-log-traffic",
        description="""Enable logging for Wire Mode traffic. Only available when Wire Mode is enabled.""",
    )
    enable_nat_traversal: bool = Field(
        alias="enable-nat-traversal",
        description="""Enable NAT traversal (NAT-T) based on RFC 3193. Switches to UDP port 4500 when NAT is detected. Not supported with Aggressive Mode.""",
    )
