from e_v_c_settings_for_gateway_request import EVCSettingsForGatewayRequest
from pydantic import BaseModel, Field


class VCSettingsForGatewayRequest(BaseModel):
    endpoint_clients_settings_for_gateway: EVCSettingsForGatewayRequest = Field(
        alias="endpoint-clients-settings-for-gateway", description="""N/A"""
    )
