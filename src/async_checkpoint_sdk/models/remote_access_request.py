from .pydantic import BaseModel, Field


class RemoteAccessRequest(BaseModel):
    support_l2tp: bool = Field(
        alias="support-l2tp",
        description="""Support L2TP (relevant only when office mode is active).""",
    )
    l2tp_auth_method: str = Field(
        alias="l2tp-auth-method",
        description="""L2TP Authentication Method.
Must be set when support-l2tp is true.""",
    )
    l2tp_certificate: str = Field(
        alias="l2tp-certificate",
        description="""L2TP Certificate.
Must be set when l2tp-auth-method was selected to be certificate.
Insert defaultCert when you want to use the default certificate.""",
    )
    allow_vpn_clients_to_route_traffic: bool = Field(
        alias="allow-vpn-clients-to-route-traffic",
        description="""Allow VPN clients to route traffic.""",
    )
    support_nat_traversal_mechanism: bool = Field(
        alias="support-nat-traversal-mechanism",
        description="""Support NAT traversal mechanism (UDP encapsulation).""",
    )
    nat_traversal_service: str = Field(
        alias="nat-traversal-service",
        description="""Allocated NAT traversal UDP service. Identified by name or UID.
Must be set when support-nat-traversal-mechanism is true.""",
    )
    support_visitor_mode: bool = Field(
        alias="support-visitor-mode", description="""Support Visitor Mode."""
    )
    visitor_mode_service: str = Field(
        alias="visitor-mode-service",
        description="""TCP Service for Visitor Mode. Identified by name or UID.
Must be set when support-visitor-mode is true.""",
    )
    visitor_mode_interface: str = Field(
        alias="visitor-mode-interface",
        description="""Interface for Visitor Mode.
Must be set when support-visitor-mode is true.
Insert IPV4 Address of existing interface or All IPs when you want all interfaces.""",
    )
