from .pydantic import BaseModel, Field


class VptSetVdInterfaceRequest(BaseModel):
    anti_spoofing: str = Field(
        alias="anti-spoofing",
        description="""The anti-spoofing enforcement setting of this interface.""",
    )
    anti_spoofing_tracking: str = Field(
        alias="anti-spoofing-tracking",
        description="""The anti-spoofing tracking setting of this interface.""",
    )
    ipv4_address: str = Field(
        alias="ipv4-address",
        description="""IPv4 Address of this interface with optional CIDR prefix.<br/>Required if this interface belongs to a Virtual System or Virtual Router.""",
    )
    ipv6_address: str = Field(
        alias="ipv6-address",
        description="""IPv6 Address of this interface<br/>Required if this interface belongs to a Virtual System or Virtual Router.""",
    )
    mtu: int = Field(alias="mtu", description="""MTU of this interface.""")
    new_leads_to: str = Field(
        alias="new-leads-to",
        description="""New Virtual Switch or Virtual Router for this interface.""",
    )
    propagate: bool = Field(
        alias="propagate",
        description="""Propagate IPv4 route to adjacent virtual devices.""",
    )
    propagate6: bool = Field(
        alias="propagate6",
        description="""Propagate IPv6 route to adjacent virtual devices.""",
    )
    specific_group: str = Field(
        alias="specific-group",
        description="""Specific group for interface topology.<br/>Only for use with topology option 'internal_specific'.""",
    )
    topology: str = Field(
        alias="topology",
        description="""Topology of this interface.<br/>Automatic topology calculation based on routes must be disabled for this VS.""",
    )
