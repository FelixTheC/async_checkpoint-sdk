from .api_object_standard_identifier import ApiObjectStandardIdentifier
from .pydantic import BaseModel, Field


class SharedSecretReply(BaseModel):
    external_gateway: ApiObjectStandardIdentifier = Field(
        alias="external-gateway", description="""External gateway."""
    )
