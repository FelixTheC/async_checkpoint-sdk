from api_domain_identifier import ApiDomainIdentifier
from pydantic import BaseModel, Field


class MdsStatObjectReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    type: str = Field(alias="type", description="""Object type.""")
    ip_address: str = Field(alias="ip-address", description="""IPv4 or IPv6 address.""")
    server_status: str = Field(alias="server-status", description="""Server status.""")
    processes: list[dict] = Field(alias="processes", description="""Server processes.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain", description="""Information about the domain that holds the Object."""
    )
