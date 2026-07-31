from .pydantic import BaseModel, Field


class ThirdPartyNatReply(BaseModel):
    enable_address_translation: bool = Field(
        alias="enable-address-translation",
        description="""Whether to enable address translation.""",
    )
    ipv4_address: str = Field(alias="ipv4-address", description="""IPv4 address.""")
    ipv6_address: str = Field(alias="ipv6-address", description="""IPv6 address.""")
    hide_behind: str = Field(
        alias="hide-behind",
        description="""Hide behind method. This parameter is forbidden in case method parameter is static.""",
    )
    automatic_nat_rules: str = Field(
        alias="automatic-nat-rules",
        description="""Whether to add automatic address translation rules.<br>checkpoint-gateway: generate automatic address translation rules using the install-on values.<br>third-party-or-cloud-gateway: don't generate automatic address translation rules for cloud and 3rd party gateways.<br> <br>Note: Supported only by Security Gateways R82 and higher.<br>For Security Gateways lower than R82 the value of the translated IP address set above will not be enforced. See sk171055 and sk171665.""",
    )
    install_on: str = Field(
        alias="install-on",
        description="""Which gateway should apply the NAT translation.""",
    )
    method: str = Field(alias="method", description="""NAT translation method.""")
    communication_with_this_server: str = Field(
        alias="communication-with-this-server",
        description="""How gateways will communicate with this server.<br> <br>Note: original-ip-only and translated-ip-only Supported only by Security Gateways R82 and higher.""",
    )
