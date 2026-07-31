from pydantic import BaseModel, Field


class CustomTrustedCaCertificateRequestNew(BaseModel):
    base64_certificate: str = Field(
        alias="base64-certificate",
        description="""Certificate file encoded in base64.<br/>Valid file formats: x509.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
