from pydantic import BaseModel, Field


class CertsAndPkiGlobalPropertiesReply(BaseModel):
    cert_validation_enforce_key_size: str = Field(
        alias="cert-validation-enforce-key-size",
        description="""Enforce key length in certificate validation (R80+ gateways only).""",
    )
    host_certs_ecdsa_key_size: str = Field(
        alias="host-certs-ecdsa-key-size",
        description="""Select the key size for ECDSA of the host certificate.""",
    )
    host_certs_key_size: str = Field(
        alias="host-certs-key-size",
        description="""Select the key size of the host certificate.""",
    )
