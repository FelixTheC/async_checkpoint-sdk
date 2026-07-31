from pydantic import BaseModel, Field


class CertificateSettingsReply(BaseModel):
    certificate: str = Field(alias="certificate", description="""The certificate.""")
    certificate_dn: str = Field(
        alias="certificate-dn", description="""The DN (Distinguished Name) of the certificate."""
    )
    certificate_valid_from: str = Field(
        alias="certificate-valid-from",
        description="""The date, from which the certificate is valid.""",
    )
    certificate_valid_to: str = Field(
        alias="certificate-valid-to", description="""The certificate expiration date."""
    )
