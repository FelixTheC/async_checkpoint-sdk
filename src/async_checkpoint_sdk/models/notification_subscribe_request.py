from .pydantic import BaseModel, Field


class NotificationSubscribeRequest(BaseModel):
    notification_type: str = Field(alias="notification-type", description="""N/A""")
    subscription_uid: str = Field(alias="subscription-uid", description="""N/A""")
