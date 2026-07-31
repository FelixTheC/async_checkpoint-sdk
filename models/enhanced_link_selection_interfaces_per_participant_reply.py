from api_object_standard_identifier import ApiObjectStandardIdentifier
from pydantic import BaseModel, Field


class EnhancedLinkSelectionInterfacesPerParticipantReply(BaseModel):
    gateway: ApiObjectStandardIdentifier = Field(
        alias="gateway", description="""Participant VPN Peer."""
    )
    interfaces: list[dict] = Field(
        alias="interfaces", description="""Enhanced Link Selection Interfaces."""
    )
