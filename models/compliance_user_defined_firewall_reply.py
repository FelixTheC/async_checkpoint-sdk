from pydantic import BaseModel, Field


class ComplianceUserDefinedFirewallReply(BaseModel):
    policy_range_percentage: int = Field(
        alias="policy-range-percentage",
        description="""User-defined policy range percentage to test.""",
    )
    policy_range_position: str = Field(
        alias="policy-range-position",
        description="""User-defined policy range position.""",
    )
    poor_condition: str = Field(
        alias="poor-condition", description="""User-defined poor condition."""
    )
    secure_condition: str = Field(
        alias="secure-condition", description="""User-defined secure condition."""
    )
    tolerance: int = Field(
        alias="tolerance",
        description="""User-defined tolerance. Appears only when the value of the 'violation-condition' parameter is 'Rule found'.""",
    )
    user_defined_rules: list[dict] = Field(
        alias="user-defined-rules", description="""User-defined Firewall rules."""
    )
    violation_condition: str = Field(
        alias="violation-condition", description="""User-defined violation condition."""
    )
