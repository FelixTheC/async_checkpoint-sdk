from pydantic import BaseModel, Field


class EVCSettingsForGatewayReply(BaseModel):
    endpoint_vpn_enable: bool = Field(
        alias="endpoint-vpn-enable",
        description="""Enables the Endpoint Security Client.""",
    )
