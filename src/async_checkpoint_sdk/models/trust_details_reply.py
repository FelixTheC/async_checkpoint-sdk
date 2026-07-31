from pydantic import BaseModel, Field
from tunnel_details_reply import TunnelDetailsReply


class TrustDetailsReply(BaseModel):
    authentication_token: str = Field(
        alias="authentication-token",
        description="""Authentication token to use on the Gateway side to establish the communication between the Gateway and the Management Server (applies only to Smart-1 Cloud).""",
    )
    cloud_communication_details: TunnelDetailsReply = Field(
        alias="cloud-communication-details",
        description="""Details about the communication status with cloud (applies only to Smart-1 Cloud).""",
    )
    gateway_mac_address: str = Field(
        alias="gateway-mac-address",
        description="""Use the Security Gateway MAC address, relevant for the gateway_mac_address identification-method.""",
    )
    identification_method: str = Field(
        alias="identification-method",
        description="""How to identify the gateway (relevant for DAIP gateways only).""",
    )
    status: str = Field(
        alias="status",
        description="""Status of the trusted communication with the Security Gateway.""",
    )
    token_expiration_date: str = Field(
        alias="token-expiration-date",
        description="""Details about the communication status with cloud (applies only to Smart-1 Cloud).""",
    )
