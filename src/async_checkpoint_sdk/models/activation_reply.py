from pydantic import BaseModel, Field


class ActivationReply(BaseModel):
    action: str = Field(alias="action", description="""Protection action.""")
    capture_packets: bool = Field(alias="capture-packets", description="""Capture packets.""")
    track: str = Field(alias="track", description="""Tracking method for protection.""")
