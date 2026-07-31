from pydantic import BaseModel, Field


class QoSGlobalPropertiesReply(BaseModel):
    default_weight_of_rule: int = Field(
        alias="default-weight-of-rule",
        description="""Define a Weight at which bandwidth will be guaranteed. Set a default weight for a rule.<br>Note: Value will be applied to new rules only.""",
    )
    max_weight_of_rule: int = Field(
        alias="max-weight-of-rule",
        description="""Define a Weight at which bandwidth will be guaranteed. Set a maximum weight for a rule.""",
    )
    unit_of_measure: str = Field(
        alias="unit-of-measure",
        description="""Define the Rate at which packets are transmitted, for which bandwidth will be guaranteed. Set a Unit of measure.""",
    )
    authenticated_ip_expiration: int = Field(
        alias="authenticated-ip-expiration",
        description="""Define the Authentication time-out for QoS. This timeout is set in minutes. In an Authenticated IP all connections which are open in a specified time limit will be guaranteed bandwidth, but will not be guaranteed bandwidth after the time limit.""",
    )
    non_authenticated_ip_expiration: int = Field(
        alias="non-authenticated-ip-expiration",
        description="""Define the Authentication time-out for QoS. This timeout is set in minutes.""",
    )
    unanswered_queried_ip_expiration: int = Field(
        alias="unanswered-queried-ip-expiration",
        description="""Define the Authentication time-out for QoS. This timeout is set in minutes.""",
    )
