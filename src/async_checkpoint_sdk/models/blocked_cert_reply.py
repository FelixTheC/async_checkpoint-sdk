from .pydantic import BaseModel, Field


class BlockedCertReply(BaseModel):
    name: str = Field(alias="name", description="""Describes the name, cannot be overridden.""")
    cert_serial_number: str = Field(
        alias="cert-serial-number",
        description="""Certificate Serial Number (unique) in hexadecimal format HH:HH.""",
    )
    comments: str = Field(
        alias="comments",
        description="""Describes the certificate by default, can be overridden by any text.""",
    )
