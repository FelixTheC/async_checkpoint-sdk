from enhanced_link_selection_interfaces_request import EnhancedLinkSelectionInterfacesRequest
from pydantic import BaseModel, Field


class EnhancedLinkSelectionInterfacesPerParticipantRequestAddAndEdit(BaseModel):
    gateway: str = Field(alias="gateway", description="""Participant VPN Peer.""")
    interfaces: EnhancedLinkSelectionInterfacesRequest | list[dict] = Field(
        alias="interfaces", description="""Enhanced Link Selection Interfaces."""
    )
