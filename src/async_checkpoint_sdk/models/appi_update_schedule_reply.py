from api_domain_identifier import ApiDomainIdentifier
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field
from schedule_update_gateway_reply import ScheduleUpdateGatewayReply
from schedule_update_mgmt_reply import ScheduleUpdateMgmtReply


class AppiUpdateScheduleReply(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    schedule_management_update: ScheduleUpdateMgmtReply = Field(
        alias="schedule-management-update",
        description="""Application Control & URL Filtering Update Schedule on Management Server.""",
    )
    schedule_gateway_update: ScheduleUpdateGatewayReply = Field(
        alias="schedule-gateway-update",
        description="""Application Control & URL Filtering Update Schedule on Gateway.""",
    )
    domain: ApiDomainIdentifier = Field(
        alias="domain", description="""Information about the domain that holds the Object."""
    )
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
