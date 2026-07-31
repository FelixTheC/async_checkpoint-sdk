from pydantic import BaseModel, Field


class MepPriorityRuleReply(BaseModel):
    satellite_gateways: list[str] = Field(
        alias="satellite-gateways",
        description="""Collection of satellite VPN Gateway and VPN Device objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    first_priority_center_gateways: list[str] = Field(
        alias="first-priority-center-gateways",
        description="""Collection of first priority center VPN Gateway and VPN Device objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    second_priority_center_gateways: list[str] = Field(
        alias="second-priority-center-gateways",
        description="""Collection of second priority center VPN Gateway and VPN Device objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    third_priority_center_gateways: list[str] = Field(
        alias="third-priority-center-gateways",
        description="""Collection of third priority center VPN Gateway and VPN Device objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
