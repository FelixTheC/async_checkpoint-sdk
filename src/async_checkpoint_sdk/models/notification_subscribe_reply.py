from .pydantic import BaseModel, Field


class NotificationSubscribeReply(BaseModel):
    subscription_uid: str = Field(alias="subscription-uid", description="""N/A""")
