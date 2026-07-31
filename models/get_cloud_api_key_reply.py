from cloud_app_status_reply import CloudAppStatusReply
from pydantic import BaseModel, Field


class GetCloudApiKeyReply(BaseModel):
    cloud_service: CloudAppStatusReply = Field(
        alias="cloud-service", description="""N/A"""
    )
