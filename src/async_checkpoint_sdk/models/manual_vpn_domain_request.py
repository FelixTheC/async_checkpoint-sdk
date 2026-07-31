from pydantic import BaseModel, Field


class ManualVpnDomainRequest(BaseModel):
    comments: str = Field(alias="comments", description="""Comments string.""")
    from_ipv4_address: str = Field(
        alias="from-ipv4-address", description="""First IPv4 address of the IP address range."""
    )
    to_ipv4_address: str = Field(
        alias="to-ipv4-address", description="""Last IPv4 address of the IP address range."""
    )
