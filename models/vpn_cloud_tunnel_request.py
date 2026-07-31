from pydantic import BaseModel, Field


class VpnCloudTunnelRequest(BaseModel):
    community: str = Field(alias="community", description="""N/A""")
    dry_run: bool = Field(alias="dry-run", description="""N/A""")
    gateways: list[str] = Field(alias="gateways", description="""N/A""")
    vpn_cloud_gateway: str = Field(alias="vpn-cloud-gateway", description="""N/A""")
