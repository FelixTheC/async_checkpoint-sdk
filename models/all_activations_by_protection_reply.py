from activation_reply import ActivationReply
from pydantic import BaseModel, Field


class AllActivationsByProtectionReply(BaseModel):
    default: ActivationReply = Field(
        alias="default", description="""Default settings."""
    )
    final: ActivationReply = Field(alias="final", description="""Final settings.""")
    override: ActivationReply = Field(
        alias="override", description="""Settings overrides."""
    )
    protection: str = Field(alias="protection", description="""IPS protection name.""")
    protection_external_info: list[str] = Field(
        alias="protection-external-info", description="""Industry reference (CVE)."""
    )
    protection_uid: str = Field(
        alias="protection-uid", description="""IPS protection unique identifier."""
    )
