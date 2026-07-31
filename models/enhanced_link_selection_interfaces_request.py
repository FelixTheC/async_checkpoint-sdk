from pydantic import BaseModel, Field


class EnhancedLinkSelectionInterfacesRequest(BaseModel):
    next_hop_ip: str = Field(
        alias="next-hop-ip", description="""The IP address of the next hop."""
    )
    static_nat_ip: str = Field(
        alias="static-nat-ip",
        description="""The NATed IPv4 address that hides the source IPv4 address of outgoing connections (applies only to IPv4).""",
    )
    priority: int = Field(
        alias="priority", description="""Priority of a 'Backup' interface."""
    )
    redundancy_mode: str = Field(
        alias="redundancy-mode",
        description="""Interface redundancy mode (Active/Backup).""",
    )
    ip_version: str = Field(
        alias="ip-version",
        description="""The IP version of the interface's IP address (IPv4/IPv6).""",
    )
