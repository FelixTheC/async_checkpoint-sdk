from pydantic import BaseModel, Field


class EnhancedLinkSelectionInterfacesRequestToRemove(BaseModel):
    interface_name: str = Field(
        alias="interface-name", description="""The name of the interface."""
    )
    ip_version: str = Field(
        alias="ip-version",
        description="""The IP version of the interface's IP address (IPv4/IPv6).""",
    )
