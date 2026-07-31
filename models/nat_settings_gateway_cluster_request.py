from pydantic import BaseModel, Field


class NatSettingsGatewayClusterRequest(BaseModel):
    apply_control_connections: bool = Field(
        alias="apply-control-connections",
        description="""This option performs NAT on VPN control connections to and from this object.""",
    )
    hide_behind: str = Field(
        alias="hide-behind",
        description="""Hide behind method. This parameter is forbidden in case method parameter is static.""",
    )
    install_on: str = Field(
        alias="install-on",
        description="""Which gateway should apply the NAT translation.""",
    )
    method: str = Field(alias="method", description="""NAT translation method.""")
