from .pydantic import BaseModel, Field


class LsmGatewaySicRequest(BaseModel):
    ip_address: str = Field(
        alias="ip-address",
        description="""IP address. When IP address is provided- initiate trusted communication immediately using this IP address.""",
    )
