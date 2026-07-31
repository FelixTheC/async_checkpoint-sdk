from .ipv4_address_range_reply import Ipv4AddressRangeReply
from .pydantic import BaseModel, Field


class ResolvedIpAddrReply(BaseModel):
    ipv4_address: str = Field(alias="ipv4-address", description="""IPv4 address.""")
    ipv4_address_range: Ipv4AddressRangeReply = Field(
        alias="ipv4-address-range", description="""IPv4 address range."""
    )
