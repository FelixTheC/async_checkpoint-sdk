from pydantic import BaseModel, Field


class ResolvedIpAddrRequest(BaseModel):
    ipv4_address: str = Field(alias="ipv4-address", description="""IPv4 Address.""")
