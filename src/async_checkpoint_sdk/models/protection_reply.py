from api_domain_identifier import ApiDomainIdentifier
from pydantic import BaseModel, Field


class ProtectionReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    comments: str = Field(alias="comments", description="""Protection comments.""")
    confidence_level: str = Field(
        alias="confidence-level",
        description="""How confident IPS is that recognized attacks are actually undesirable traffic.""",
    )
    follow_up: bool = Field(
        alias="follow-up", description="""Tag the protection with pre-defined follow-up flag."""
    )
    industry_reference: list[str] = Field(
        alias="industry-reference",
        description="""International CVE or CVE candidate name for attack.""",
    )
    ipsadditionalproperties: list[dict] = Field(
        alias="ipsAdditionalProperties", description="""IPS protection extended attributes."""
    )
    performance_impact: str = Field(
        alias="performance-impact",
        description="""How much this protection affects the performance of a Security Gateway.""",
    )
    profiles: list[dict] = Field(
        alias="profiles", description="""Protection settings per profile."""
    )
    protection_type: str = Field(
        alias="protection-type", description="""The protection's type (Core or Threat Cloud)."""
    )
    release_date: str = Field(
        alias="release-date",
        description="""The date in which the protection was releases by Check Point.""",
    )
    severity: str = Field(alias="severity", description="""The intrusion severity.""")
    update_date: str = Field(
        alias="update-date",
        description="""The date in which the protection was updated by Check Point.""",
    )
    domain: ApiDomainIdentifier = Field(
        alias="domain", description="""Information about the domain that holds the Object."""
    )
