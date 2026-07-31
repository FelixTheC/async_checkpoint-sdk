from .pydantic import BaseModel, Field


class VptRemoveRouteRequest(BaseModel):
    netmask: str = Field(alias="netmask", description="""Subnet mask for this route.""")
    prefix: str = Field(alias="prefix", description="""CIDR prefix for this route.""")
