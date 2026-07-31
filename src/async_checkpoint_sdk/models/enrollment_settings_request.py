from alternate_names_request import AlternateNamesRequest
from pydantic import BaseModel, Field


class EnrollmentSettingsRequest(BaseModel):
    distinguished_name: str = Field(
        alias="distinguished-name",
        description="""The Distinguished Name of the certificate. If the certificate-authority type is external, the Distinguished Name must start with CN=.""",
    )
    alternate_names: AlternateNamesRequest | list[dict] = Field(
        alias="alternate-names", description="""Certificate alternate names."""
    )
