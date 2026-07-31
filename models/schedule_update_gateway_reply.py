from pydantic import BaseModel, Field
from schedule_conf_gateway_reply import ScheduleConfGatewayReply


class ScheduleUpdateGatewayReply(BaseModel):
    enabled: bool = Field(
        alias="enabled",
        description="""Enable/Disable Application Control & URL Filtering Update Schedule on Gateway.""",
    )
    schedule: ScheduleConfGatewayReply = Field(
        alias="schedule", description="""Schedule Configuration."""
    )
