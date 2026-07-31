from .pydantic import BaseModel, Field


class StarRimReply(BaseModel):
    enabled: bool = Field(
        alias="enabled",
        description="""Indicates whether Route Injection Mechanism is enabled.""",
    )
    enable_on_center_gateways: bool = Field(
        alias="enable-on-center-gateways",
        description="""Indicates whether to enable automatic Route Injection Mechanism on center gateways.""",
    )
    enable_on_satellite_gateways: bool = Field(
        alias="enable-on-satellite-gateways",
        description="""Indicates whether to enable automatic Route Injection Mechanism on satellite gateways.""",
    )
    route_injection_track: str = Field(
        alias="route-injection-track", description="""Route injection track method."""
    )
