from pydantic import BaseModel, Field


class EnhancedLinkSelectionInterfacesRequestToRemove(BaseModel):
    ip_version: str = Field(
        alias="ip-version",
        description="""The IP version of the interface's IP address (IPv4/IPv6).""",
    )
