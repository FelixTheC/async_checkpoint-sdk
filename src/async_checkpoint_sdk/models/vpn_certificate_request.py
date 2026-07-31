from certificate_enrollment_request import CertificateEnrollmentRequest
from pydantic import BaseModel, Field


class VpnCertificateRequest(BaseModel):
    name: str = Field(alias="name", description="""Certificate name.""")
    certificate_authority: str = Field(
        alias="certificate-authority",
        description="""Certificate authority to enroll from. Identified by the Name or UID.""",
    )
    enrollment: CertificateEnrollmentRequest = Field(
        alias="enrollment", description="""Certificate enrollment."""
    )
    stored_at: str = Field(
        alias="stored-at",
        description="""Store keys on Security Management Server or on the Gateway. Default value is management server. On cluster object only management server is valid.""",
    )
