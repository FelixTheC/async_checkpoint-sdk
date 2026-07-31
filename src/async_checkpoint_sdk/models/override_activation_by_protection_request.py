from pydantic import BaseModel, Field


class OverrideActivationByProtectionRequest(BaseModel):
    action: str = Field(alias="action", description="""Protection action.""")
    protection: str = Field(
        alias="protection", description="""IPS protection identified by name or UID."""
    )
    capture_packets: bool = Field(alias="capture-packets", description="""Capture packets.""")
    track: str = Field(alias="track", description="""Tracking method for protection.""")
