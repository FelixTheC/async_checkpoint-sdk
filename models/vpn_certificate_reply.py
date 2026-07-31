from api_date_reply import ApiDateReply
from api_domain_identifier import ApiDomainIdentifier
from api_object_standard_identifier import ApiObjectStandardIdentifier
from pydantic import BaseModel, Field


class VpnCertificateReply(BaseModel):
    name: str = Field(alias="name", description="""Certificate name.""")
    distinguished_name: str = Field(
        alias="distinguished-name",
        description="""The Distinguished Name of the certificate.""",
    )
    type: str = Field(alias="type", description="""Object type.""")
    base64_certificate: str = Field(
        alias="base64-certificate",
        description="""Certificate file encoded in base64.""",
    )
    certificate_authority: ApiObjectStandardIdentifier = Field(
        alias="certificate-authority", description="""Certificate Authority."""
    )
    expiration_date: ApiDateReply = Field(
        alias="expiration-date", description="""Certificate expiration date."""
    )
    status: str = Field(alias="status", description="""Certificate status.""")
    stored_at: str = Field(
        alias="stored-at",
        description="""Store keys on Security Management Server or on the Gateway. On cluster object only management server is valid.""",
    )
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
