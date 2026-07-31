from .pydantic import BaseModel, Field


class NatSettingsReply(BaseModel):
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
