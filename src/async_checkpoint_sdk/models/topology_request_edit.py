from .add import add
from .manual_vpn_domain_request import ManualVpnDomainRequest
from .pydantic import BaseModel, Field
from .remove import remove


class TopologyRequestEdit(BaseModel):
    manual_vpn_domain: add | remove | ManualVpnDomainRequest | list[dict] = Field(
        alias="manual-vpn-domain",
        description="""A list of IP-addresses ranges, defined the VPN community network.
This field is relevant only when 'manual' option of vpn-domain is checked.""",
    )
    vpn_domain: str = Field(
        alias="vpn-domain",
        description="""VPN Domain type.
 'external-interfaces-only' is relevnt only for Gaia devices.
'hide-behind-gateway-external-ip-address' is relevant only for SMB devices.""",
    )
