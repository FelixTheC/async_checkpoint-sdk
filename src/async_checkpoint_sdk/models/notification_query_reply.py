from .pydantic import BaseModel, Field


class NotificationQueryReply(BaseModel):
    notifications: list[dict] = Field(alias="notifications", description="""N/A""")
    total: int = Field(alias="total", description="""N/A""")
