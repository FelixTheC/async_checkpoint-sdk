from .add import add
from .pydantic import BaseModel, Field
from .remove import remove


class DefaultMepPriorityRuleRequestEdit(BaseModel):
    first_priority_center_gateways: str | add | remove | str | list[str] = Field(
        alias="first-priority-center-gateways",
        description="""Collection of first priority center gateways identified by the name or UID.""",
    )
    second_priority_center_gateways: str | add | remove | str | list[str] = Field(
        alias="second-priority-center-gateways",
        description="""Collection of second priority center gateways identified by the name or UID.""",
    )
    third_priority_center_gateways: str | add | remove | str | list[str] = Field(
        alias="third-priority-center-gateways",
        description="""Collection of third priority center gateways identified by the name or UID.""",
    )
