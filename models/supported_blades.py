from pydantic import BaseModel, Field
from threat_prevention_blades import ThreatPreventionBlades


class SupportedBlades(BaseModel):
    management: list[dict] = Field(
        alias="management", description="""Management blades."""
    )
    network_security: list[dict] = Field(
        alias="network-security", description="""Network Security blades."""
    )
    threat_prevention: ThreatPreventionBlades = Field(
        alias="threat-prevention", description="""Threat Prevention blades."""
    )
