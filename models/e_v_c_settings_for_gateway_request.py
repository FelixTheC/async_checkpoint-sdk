from pydantic import BaseModel, Field


class EVCSettingsForGatewayRequest(BaseModel):
    endpoint_vpn_enable: bool = Field(
        alias="endpoint-vpn-enable", description="""N/A"""
    )
