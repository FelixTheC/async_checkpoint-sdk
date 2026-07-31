from api_object_standard_identifier import ApiObjectStandardIdentifier
from pydantic import BaseModel, Field


class RadiusAccountingObjectReply(BaseModel):
    enable_ip_pool_management: bool = Field(
        alias="enable-ip-pool-management",
        description="""IP pool management, enables Accounting service.""",
    )
    accounting_service: ApiObjectStandardIdentifier = Field(
        alias="accounting-service",
        description="""The UID or Name of the accounting interface to notify the server when users login and logout which will then lock and release the IP addresses that the server allocated to those users.""",
    )
