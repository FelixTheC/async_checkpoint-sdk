from .api_object_standard_identifier import ApiObjectStandardIdentifier
from .pydantic import BaseModel, Field


class ParticipantsDomainsReplay(BaseModel):
    gateway: ApiObjectStandardIdentifier = Field(
        alias="gateway", description="""Participant gateway in override VPN domain."""
    )
    vpn_domain: ApiObjectStandardIdentifier = Field(
        alias="vpn-domain",
        description="""<html>VPN domain network.<br><b>Relevant only in Domain-Based VPN Communities</b></html>.""",
    )
