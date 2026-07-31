from pydantic import BaseModel, Field
from vpn_certificate_complete_request import VpnCertificateCompleteRequest


class complete(BaseModel):
    complete: VpnCertificateCompleteRequest = Field(
        alias="complete",
        description="""Completes certificate from collection of certificates""",
    )
