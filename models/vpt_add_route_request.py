from pydantic import BaseModel, Field


class VptAddRouteRequest(BaseModel):
    netmask: str = Field(alias="netmask", description="""Subnet mask for this route.""")
    prefix: str = Field(alias="prefix", description="""CIDR prefix for this route.""")
    propagate: bool = Field(
        alias="propagate",
        description="""Propagate this route to adjacent virtual devices.""",
    )
