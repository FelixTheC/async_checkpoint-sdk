from pydantic import BaseModel, Field
from resolved_ip_addr_request import ResolvedIpAddrRequest


class DynamicObjectRequestNew(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    resolved_ip_addresses: ResolvedIpAddrRequest | list[dict] = Field(
        alias="resolved-ip-addresses", description="""Single IP-address or a range of addresses."""
    )
