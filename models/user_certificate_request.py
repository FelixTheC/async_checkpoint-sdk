from p12_certificate_file_request import P12CertificateFileRequest
from pydantic import BaseModel, Field


class UserCertificateRequest(BaseModel):
    certificate_file: P12CertificateFileRequest = Field(
        alias="certificate-file", description="""Certificate file (.P12)."""
    )
