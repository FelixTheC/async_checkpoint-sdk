from .api_object_standard_identifier import ApiObjectStandardIdentifier
from .pydantic import BaseModel, Field


class AdvancedActionSettingsReply(BaseModel):
    enable_identity_captive_portal: bool = Field(
        alias="enable-identity-captive-portal", description="""N/A"""
    )
    limit: ApiObjectStandardIdentifier = Field(
        alias="limit",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
