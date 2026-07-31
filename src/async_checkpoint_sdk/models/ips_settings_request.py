from pydantic import BaseModel, Field


class IpsSettingsRequest(BaseModel):
    exclude_protection_with_performance_impact: bool = Field(
        alias="exclude-protection-with-performance-impact",
        description="""Whether to exclude protections depending on their level of performance impact.""",
    )
    exclude_protection_with_performance_impact_mode: str = Field(
        alias="exclude-protection-with-performance-impact-mode",
        description="""Exclude protections with this level of performance impact.""",
    )
    exclude_protection_with_severity: bool = Field(
        alias="exclude-protection-with-severity",
        description="""Whether to exclude protections depending on their level of severity.""",
    )
    exclude_protection_with_severity_mode: str = Field(
        alias="exclude-protection-with-severity-mode",
        description="""Exclude protections with this level of severity.""",
    )
    newly_updated_protections: str = Field(
        alias="newly-updated-protections",
        description="""Activation of newly updated protections.""",
    )
