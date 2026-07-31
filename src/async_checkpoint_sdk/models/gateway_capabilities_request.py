from .pydantic import BaseModel, Field


class GatewayCapabilitiesRequest(BaseModel):
    hardware: str = Field(alias="hardware", description="""Check Point hardware.""")
    hardware_subtype: str = Field(
        alias="hardware-subtype",
        description="""Gateway type (relevant only for Spark gateways).""",
    )
    platform: str = Field(alias="platform", description="""Check Point gateway platform.""")
    version: str = Field(alias="version", description="""Gateway platform version.""")
