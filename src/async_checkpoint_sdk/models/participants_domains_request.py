from .pydantic import BaseModel, Field


class ParticipantsDomainsRequest(BaseModel):
    gateway: str = Field(
        alias="gateway",
        description="""Participant gateway in override VPN domain identified by the name or UID.""",
    )
    vpn_domain: str = Field(
        alias="vpn-domain",
        description="""<html>VPN domain network.<br><b>Relevant only in Domain-Based VPN Communities</b></html> identified by the name or UID.""",
    )
