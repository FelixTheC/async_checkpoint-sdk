from pydantic import BaseModel, Field


class LsmGatewaySicRequest(BaseModel):
    one_time_password: str = Field(
        alias="one-time-password",
        description="""One-time password. When one-time password is provided without ip-address- trusted communication is automatically initiated  when the gateway connects to the Security Management server for the first time.""",
    )
    ip_address: str = Field(
        alias="ip-address",
        description="""IP address. When IP address is provided- initiate trusted communication immediately using this IP address.""",
    )
