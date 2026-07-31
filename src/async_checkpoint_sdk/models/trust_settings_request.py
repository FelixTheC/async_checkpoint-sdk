from .pydantic import BaseModel, Field


class TrustSettingsRequest(BaseModel):
    gateway_mac_address: str = Field(
        alias="gateway-mac-address",
        description="""Use the Security Gateway MAC address, relevant for the gateway_mac_address identification-method.""",
    )
    identification_method: str = Field(
        alias="identification-method",
        description="""How to identify the gateway (relevant for Spark DAIP gateways only).""",
    )
    initiation_phase: str = Field(
        alias="initiation-phase",
        description="""Push the certificate to the Security Gateway immediately, or wait for the Security Gateway to pull the certificate. Default value for Spark Gateway is 'when_gateway_connects'.""",
    )
