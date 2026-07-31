from .pydantic import BaseModel, Field
from .schedule_update_gateway_request_edit import ScheduleUpdateGatewayRequestEdit
from .schedule_update_mgmt_request_edit import ScheduleUpdateMgmtRequestEdit


class AppiUpdateScheduleRequestEdit(BaseModel):
    schedule_management_update: ScheduleUpdateMgmtRequestEdit = Field(
        alias="schedule-management-update",
        description="""Application Control & URL Filtering Update Schedule on Management Server.""",
    )
    schedule_gateway_update: ScheduleUpdateGatewayRequestEdit = Field(
        alias="schedule-gateway-update",
        description="""Application Control & URL Filtering Update Schedule on Gateway.""",
    )
