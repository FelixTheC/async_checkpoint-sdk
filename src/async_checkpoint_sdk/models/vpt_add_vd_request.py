from pydantic import BaseModel, Field
from vpt_add_interface_object_request import VptAddInterfaceObjectRequest
from vpt_add_route_object_request import VptAddRouteObjectRequest


class VptAddVdRequest(BaseModel):
    interfaces: VptAddInterfaceObjectRequest | list[dict] = Field(
        alias="interfaces",
        description="""The list of interfaces for this new Virtual Device.<br/>Optional if this new VD is a Virtual Switch.""",
    )
    type: str = Field(
        alias="type",
        description="""Type of the Virtual Device <br><br>vs - Virtual Firewall<br>vr - Virtual Router<br>vsw - Virtual Switch<br>vsbm - Virtual Firewall in bridge mode.""",
    )
    vd: str = Field(
        alias="vd", description="""Name of the Virtual System, Virtual Switch, or Virtual Router."""
    )
    vsx_name: str = Field(
        alias="vsx-name", description="""Name of the VSX Gateway or Cluster object."""
    )
    calc_topology_auto: bool = Field(
        alias="calc-topology-auto",
        description="""Calculate interface topology automatically based on routes.<br/>Relevant only for Virtual Systems.<br/>Do not use for virtual devices.""",
    )
    ipv4_address: str = Field(
        alias="ipv4-address",
        description="""Main IPv4 Address.<br/>Required if this device is a Virtual System.<br/>Do not use for other virtual devices.""",
    )
    ipv4_instances: int = Field(
        alias="ipv4-instances",
        description="""Number of IPv4 instances for the Virtual System.<br/>Must be greater or equal to 1.<br/>Only relevant for Virtual Systems and Virtual Systems in bridge mode.""",
    )
    ipv6_address: str = Field(
        alias="ipv6-address",
        description="""Main IPv6 Address.<br/>Required if this device is a Virtual System.<br/>Do not use for other virtual devices.""",
    )
    ipv6_instances: int = Field(
        alias="ipv6-instances",
        description="""Number of IPv6 instances for the Virtual System.<br/>Only relevant for Virtual Systems and Virtual Systems in bridge mode.""",
    )
    routes: VptAddRouteObjectRequest | list[dict] = Field(
        alias="routes",
        description="""The list of routes for this new Virtual Device (VS or VR only).""",
    )
    vs_mtu: int = Field(
        alias="vs-mtu",
        description="""MTU of the Virtual System.<br/>Only relevant for Virtual Systems in bridge mode.<br/>Do not use for other virtual devices.""",
    )
