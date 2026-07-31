from cpuuid import CPUUID
from pydantic import BaseModel, Field


class NotificationUnsubscribeRequest(BaseModel):
    subscription_uid: CPUUID = Field(alias="subscription-uid", description="""N/A""")
