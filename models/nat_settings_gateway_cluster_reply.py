from pydantic import BaseModel, Field


class NatSettingsGatewayClusterReply(BaseModel):
    apply_control_connections: bool = Field(
        alias="apply-control-connections",
        description="""This option performs NAT on VPN control connections to and from this object.""",
    )
    auto_rule: bool = Field(
        alias="auto-rule",
        description="""Whether to add automatic address translation rules.""",
    )
    hide_behind: str = Field(
        alias="hide-behind",
        description="""Hide behind method. This parameter is forbidden in case method parameter is static.""",
    )
    install_on: str = Field(
        alias="install-on",
        description="""Which gateway should apply the NAT translation.""",
    )
    ipv4_address: str = Field(alias="ipv4-address", description="""IPv4 address.""")
    ipv6_address: str = Field(alias="ipv6-address", description="""IPv6 address.""")
    method: str = Field(alias="method", description="""NAT translation method.""")
