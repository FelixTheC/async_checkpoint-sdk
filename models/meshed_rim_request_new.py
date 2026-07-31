from pydantic import BaseModel, Field


class MeshedRimRequestNew(BaseModel):
    enabled: bool = Field(
        alias="enabled",
        description="""Indicates whether Route Injection Mechanism is enabled.""",
    )
    enable_on_gateways: bool = Field(
        alias="enable-on-gateways",
        description="""Indicates whether to enable automatic Route Injection Mechanism for gateways.""",
    )
    route_injection_track: str = Field(
        alias="route-injection-track", description="""Route injection track method."""
    )
