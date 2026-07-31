from api_domain_identifier import ApiDomainIdentifier
from pydantic import BaseModel, Field


class AddressRangeStandardReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    ipv4_address_first: str = Field(
        alias="ipv4-address-first", description="""First IPv4 address in the range."""
    )
    ipv4_address_last: str = Field(
        alias="ipv4-address-last", description="""Last IPv4 address in the range."""
    )
    ipv6_address_first: str = Field(
        alias="ipv6-address-first", description="""First IPv6 address in the range."""
    )
    ipv6_address_last: str = Field(
        alias="ipv6-address-last", description="""Last IPv6 address in the range."""
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    domain: ApiDomainIdentifier = Field(
        alias="domain", description="""Information about the domain that holds the Object."""
    )
    icon: str = Field(alias="icon", description="""Object icon.""")
