from .pydantic import BaseModel, Field


class OverrideActivationByProfileRequest(BaseModel):
    capture_packets: bool = Field(alias="capture-packets", description="""Capture packets.""")
    track: str = Field(alias="track", description="""Tracking method for protection.""")
