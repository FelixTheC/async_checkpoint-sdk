from pydantic import BaseModel, Field


class IpAddressRangeRequest(BaseModel):
    address_type: str = Field(alias="address-type", description="""The type of the IP Address.""")
    first_ipv4_address: str = Field(
        alias="first-ipv4-address", description="""The first IPV4 Address in the range."""
    )
    last_ipv4_address: str = Field(
        alias="last-ipv4-address", description="""The last IPV4 Address in the range."""
    )
