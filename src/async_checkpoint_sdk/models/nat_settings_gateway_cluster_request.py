from pydantic import BaseModel, Field


class NatSettingsGatewayClusterRequest(BaseModel):
    auto_rule: bool = Field(
        alias="auto-rule", description="""Whether to add automatic address translation rules."""
    )
    ip_address: str = Field(
        alias="ip-address",
        description="""IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly. This parameter is not required in case method parameter is hide and hide-behind parameter is gateway.""",
    )
    apply_control_connections: bool = Field(
        alias="apply-control-connections",
        description="""This option performs NAT on VPN control connections to and from this object.""",
    )
    hide_behind: str = Field(
        alias="hide-behind",
        description="""Hide behind method. This parameter is forbidden in case method parameter is static.""",
    )
    install_on: str = Field(
        alias="install-on", description="""Which gateway should apply the NAT translation."""
    )
    method: str = Field(alias="method", description="""NAT translation method.""")
