from pydantic import BaseModel, Field


class FwRuleConditionTypeReply(BaseModel):
    condition_type: str = Field(alias="condition-type", description="""The condition type.""")
    value: str = Field(
        alias="value",
        description="""The condition match string. Appears only when the value of the 'condition-type' parameter is: 'Equals', 'Starts with', 'Ends with', 'Contains'.""",
    )
