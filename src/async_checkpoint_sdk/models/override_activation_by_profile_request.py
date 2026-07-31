from pydantic import BaseModel, Field


class OverrideActivationByProfileRequest(BaseModel):
    action: str = Field(alias="action", description="""Protection action.""")
    profile: str = Field(alias="profile", description="""Profile name.""")
    capture_packets: bool = Field(alias="capture-packets", description="""Capture packets.""")
    track: str = Field(alias="track", description="""Tracking method for protection.""")
