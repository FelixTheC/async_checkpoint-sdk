from .pydantic import BaseModel, Field


class ThreatRuleTrackSettingsRequest(BaseModel):
    forensics: bool = Field(alias="forensics", description="""Whether to enable forensics.""")
    packet_capture: bool = Field(alias="packet-capture", description="""Packet capture.""")
