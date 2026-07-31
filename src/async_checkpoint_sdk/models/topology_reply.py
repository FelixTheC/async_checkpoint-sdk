from .pydantic import BaseModel, Field


class TopologyReply(BaseModel):
    manual_vpn_domain: list[dict] = Field(
        alias="manual-vpn-domain", description="""Manual VPN domain."""
    )
    vpn_domain: str = Field(alias="vpn-domain", description="""VPN domain type.""")
