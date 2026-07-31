from pydantic import BaseModel, Field


class CertificateSettingsRequest(BaseModel):
    base64_certificate: str = Field(
        alias="base64-certificate",
        description="""The certificate file encoded in Base64 with padding. 
This file must be in the *.p12 format.""",
    )
    base64_password: str = Field(
        alias="base64-password",
        description="""Password (encoded in Base64 with padding) for the certificate file.""",
    )
