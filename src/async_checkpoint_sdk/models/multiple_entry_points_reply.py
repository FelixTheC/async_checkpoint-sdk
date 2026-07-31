from default_mep_priority_rule_reply import DefaultMepPriorityRuleReply
from pydantic import BaseModel, Field


class MultipleEntryPointsReply(BaseModel):
    enabled: bool = Field(
        alias="enabled", description="""Enable center gateways as Multiple Entry Points."""
    )
    entry_point_selection_mechanism: str = Field(
        alias="entry-point-selection-mechanism",
        description="""The method by which the entry point gateway will be chosen from the gateways in the center.""",
    )
    entry_point_final_selection_mechanism: str = Field(
        alias="entry-point-final-selection-mechanism",
        description="""The method by which the final entry point gateway will be chosen when the chosen mechanism returns more than one optional entry point.""",
    )
    tracking: str = Field(alias="tracking", description="""Tracking option for the MEP.""")
    default_priority_rule: DefaultMepPriorityRuleReply = Field(
        alias="default-priority-rule",
        description="""Priority rule for all satellite gateways. Relevant only if 'entry-point-selection-mechanism' is set to 'manual'.""",
    )
    exception_priority_rules: list[dict] = Field(
        alias="exception-priority-rules",
        description="""Exception priority rules for specific satellites gateways. Relevant only if 'entry-point-selection-mechanism' is set to 'manual'.""",
    )
