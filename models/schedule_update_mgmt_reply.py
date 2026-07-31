from pydantic import BaseModel, Field
from schedule_conf_mgmt_reply import ScheduleConfMgmtReply


class ScheduleUpdateMgmtReply(BaseModel):
    enabled: bool = Field(
        alias="enabled",
        description="""Enable/Disable Application Control & URL Filtering Update Schedule on Management Server.""",
    )
    schedule: ScheduleConfMgmtReply = Field(
        alias="schedule", description="""Schedule Configuration."""
    )
