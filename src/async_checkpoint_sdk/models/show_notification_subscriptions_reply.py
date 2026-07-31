from .map import Map
from .pydantic import BaseModel, Field


class ShowNotificationSubscriptionsReply(BaseModel):
    subscriptions: Map = Field(alias="subscriptions", description="""N/A""")
