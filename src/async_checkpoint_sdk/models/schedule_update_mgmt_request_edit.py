from .pydantic import BaseModel, Field
from .schedule_conf_mgmt_request_edit import ScheduleConfMgmtRequestEdit


class ScheduleUpdateMgmtRequestEdit(BaseModel):
    enabled: bool = Field(
        alias="enabled",
        description="""Enable/Disable Application Control & URL Filtering Update Schedule on Management Server.""",
    )
    schedule: ScheduleConfMgmtRequestEdit = Field(
        alias="schedule", description="""Schedule Configuration."""
    )
