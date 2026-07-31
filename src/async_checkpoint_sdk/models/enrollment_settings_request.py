from .alternate_names_request import AlternateNamesRequest
from .pydantic import BaseModel, Field


class EnrollmentSettingsRequest(BaseModel):
    alternate_names: AlternateNamesRequest | list[dict] = Field(
        alias="alternate-names", description="""Certificate alternate names."""
    )
