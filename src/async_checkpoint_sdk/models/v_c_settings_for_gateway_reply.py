from .e_v_c_settings_for_gateway_reply import EVCSettingsForGatewayReply
from .pydantic import BaseModel, Field


class VCSettingsForGatewayReply(BaseModel):
    endpoint_clients_settings_for_gateway: EVCSettingsForGatewayReply = Field(
        alias="endpoint-clients-settings-for-gateway",
        description="""Endpoint clients settings for gateway.""",
    )
