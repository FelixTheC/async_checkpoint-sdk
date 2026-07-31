from pydantic import BaseModel, Field
from schedule_conf_gateway_request_edit import ScheduleConfGatewayRequestEdit


class ScheduleUpdateGatewayRequestEdit(BaseModel):
    enabled: bool = Field(
        alias="enabled",
        description="""Enable/Disable Application Control & URL Filtering Update Schedule on Gateway.""",
    )
    schedule: ScheduleConfGatewayRequestEdit = Field(
        alias="schedule", description="""Schedule Configuration."""
    )
