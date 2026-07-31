from pydantic import BaseModel, Field


class ClientlessVpnSettingsRequest(BaseModel):
    certificate_gateway_authentication: str = Field(
        alias="certificate-gateway-authentication",
        description="""The Gateway authenticates with this Certificate.""",
    )
    client_authentication: str = Field(
        alias="client-authentication",
        description="""Client authentication type for clientless VPN.""",
    )
    concurrent_servers_or_processes: int = Field(
        alias="concurrent-servers-or-processes",
        description="""Number of servers/processes for clientless VPN. Range: 1-10.""",
    )
    accept_only_3des: bool = Field(
        alias="accept-only-3des", description="""Accept only 3DES for clientless VPN."""
    )
