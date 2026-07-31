from add import Add
from pydantic import BaseModel, Field
from remove import Remove


class MepPriorityRuleRequestEdit(BaseModel):
    rule_identifier: str = Field(
        alias="rule-identifier",
        description="""Satellite gateway to identify the priority rule. <br> 
Identified by name or UID.""",
    )
    satellite_gateways: str | Add | Remove | str | list[str] = Field(
        alias="satellite-gateways",
        description="""Collection of satellite gateways to apply priority rules on identified by the name or UID.""",
    )
    first_priority_center_gateways: str | Add | Remove | str | list[str] = Field(
        alias="first-priority-center-gateways",
        description="""Collection of first priority center gateways identified by the name or UID.""",
    )
    second_priority_center_gateways: str | Add | Remove | str | list[str] = Field(
        alias="second-priority-center-gateways",
        description="""Collection of second priority center gateways identified by the name or UID.""",
    )
    third_priority_center_gateways: str | Add | Remove | str | list[str] = Field(
        alias="third-priority-center-gateways",
        description="""Collection of third priority center gateways identified by the name or UID.""",
    )
