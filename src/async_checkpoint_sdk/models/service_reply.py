from object import Object
from pydantic import BaseModel, Field


class ServiceReply(BaseModel):
    service_reply: Object = Field(alias="service-reply", description="""N/A""")
