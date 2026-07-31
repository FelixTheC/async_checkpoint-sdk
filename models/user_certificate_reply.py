from api_date_reply import ApiDateReply
from pydantic import BaseModel, Field


class UserCertificateReply(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    status: str = Field(alias="status", description="""Certificate status.""")
    subject: str = Field(alias="subject", description="""Certificate subject.""")
    valid_to: ApiDateReply = Field(alias="valid-to", description="""Expiration date.""")
    comments: str = Field(alias="comments", description="""Certificate comments.""")
    base64_certificate: str = Field(
        alias="base64-certificate",
        description="""Certificate file encoded in base64.<br/>File format: .P12.""",
    )
    registration_key: str = Field(
        alias="registration-key", description="""Registration key for enrollment."""
    )
