from pydantic import BaseModel, Field
from resolved_ip_addr_request import ResolvedIpAddrRequest


class DynamicObjectRequestNew(BaseModel):
    resolved_ip_addresses: ResolvedIpAddrRequest | list[dict] = Field(
        alias="resolved-ip-addresses",
        description="""Single IP-address or a range of addresses.""",
    )
