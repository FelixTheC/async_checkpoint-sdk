from api_domain_identifier import ApiDomainIdentifier
from pydantic import BaseModel, Field


class HostStandardReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    ipv4_address: str = Field(alias="ipv4-address", description="""IPv4 host address.""")
    ipv6_address: str = Field(alias="ipv6-address", description="""IPv6 host address.""")
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    domain: ApiDomainIdentifier = Field(
        alias="domain", description="""Information about the domain that holds the Object."""
    )
    icon: str = Field(alias="icon", description="""Object icon.""")
