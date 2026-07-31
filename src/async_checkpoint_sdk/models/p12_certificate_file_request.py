from .pydantic import BaseModel, Field


class P12CertificateFileRequest(BaseModel):
    comment: str = Field(alias="comment", description="""Certificate comment.""")
