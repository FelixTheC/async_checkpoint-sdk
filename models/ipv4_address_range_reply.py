from pydantic import BaseModel, Field


class Ipv4AddressRangeReply(BaseModel):
    from_ipv4_address: str = Field(
        alias="from-ipv4-address", description="""From IPv4 Address."""
    )
    to_ipv4_address: str = Field(
        alias="to-ipv4-address", description="""To IPv4 Address."""
    )
