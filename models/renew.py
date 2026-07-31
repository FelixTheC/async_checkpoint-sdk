from pydantic import BaseModel, Field
from vpn_certificate_renew_request import VpnCertificateRenewRequest


class renew(BaseModel):
    renew: VpnCertificateRenewRequest = Field(
        alias="renew",
        description="""Renews certificate from collection of certificates""",
    )
