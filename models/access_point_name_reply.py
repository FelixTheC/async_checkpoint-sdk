from api_object_standard_identifier import ApiObjectStandardIdentifier
from pydantic import BaseModel, Field


class AccessPointNameReply(BaseModel):
    enable: bool = Field(alias="enable", description="""""")
    apn: ApiObjectStandardIdentifier = Field(
        alias="apn",
        description="""The Access Point Name object identified by Name or UID.""",
    )
