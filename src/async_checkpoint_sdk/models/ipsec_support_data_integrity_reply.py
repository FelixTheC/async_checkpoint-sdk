from .pydantic import BaseModel, Field


class IpsecSupportDataIntegrityReply(BaseModel):
    aes_xcbc: bool = Field(
        alias="aes-xcbc",
        description="""Select whether the AES-XCBC hash algorithm will be supported with remote hosts to ensure data integrity.""",
    )
    md5: bool = Field(
        alias="md5",
        description="""Select whether the MD5 hash algorithm will be supported with remote hosts to ensure data integrity.""",
    )
    sha1: bool = Field(
        alias="sha1",
        description="""Select whether the SHA1 hash algorithm will be supported with remote hosts to ensure data integrity.""",
    )
    sha256: bool = Field(
        alias="sha256",
        description="""Select whether the SHA256 hash algorithm will be supported with remote hosts to ensure data integrity.""",
    )
    sha384: bool = Field(
        alias="sha384",
        description="""Select whether the SHA384 hash algorithm will be supported with remote hosts to ensure data integrity.""",
    )
    sha512: bool = Field(
        alias="sha512",
        description="""Select whether the SHA512 hash algorithm will be supported with remote hosts to ensure data integrity.""",
    )
