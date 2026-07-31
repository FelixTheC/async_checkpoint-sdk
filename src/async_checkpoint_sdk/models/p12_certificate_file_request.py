from pydantic import BaseModel, Field


class P12CertificateFileRequest(BaseModel):
    password: str = Field(alias="password", description="""Password of the certificate file.""")
    comment: str = Field(alias="comment", description="""Certificate comment.""")
