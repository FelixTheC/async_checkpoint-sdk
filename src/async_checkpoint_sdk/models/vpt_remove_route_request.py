from pydantic import BaseModel, Field


class VptRemoveRouteRequest(BaseModel):
    destination: str = Field(
        alias="destination",
        description="""Route destination. To specify the default route, use 'default' for IPv4 and 'default6' for IPv6.""",
    )
    vd: str = Field(
        alias="vd", description="""Name of the Virtual System, Virtual Switch, or Virtual Router."""
    )
    netmask: str = Field(alias="netmask", description="""Subnet mask for this route.""")
    prefix: str = Field(alias="prefix", description="""CIDR prefix for this route.""")
