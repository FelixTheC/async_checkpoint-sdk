from api_object_standard_identifier import ApiObjectStandardIdentifier
from pydantic import BaseModel, Field


class OutboundCertificateOverrideReply(BaseModel):
    override_profile: bool = Field(
        alias="override-profile",
        description="""Override profile of global configuration.""",
    )
    profile_value: ApiObjectStandardIdentifier = Field(
        alias="profile-value", description="""Override profile value."""
    )
    value: ApiObjectStandardIdentifier = Field(
        alias="value", description="""Override value."""
    )
