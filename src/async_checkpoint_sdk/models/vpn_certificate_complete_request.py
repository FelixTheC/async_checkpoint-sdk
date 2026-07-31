from pydantic import BaseModel, Field


class VpnCertificateCompleteRequest(BaseModel):
    name: str = Field(alias="name", description="""Certificate name.""")
    base64_certificate: str = Field(
        alias="base64-certificate", description="""Certificate file encoded in base64."""
    )
