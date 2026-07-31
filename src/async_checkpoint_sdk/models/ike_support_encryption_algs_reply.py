from pydantic import BaseModel, Field


class IkeSupportEncryptionAlgsReply(BaseModel):
    aes_128: bool = Field(
        alias="aes-128",
        description="""Select whether the AES-128 encryption algorithm will be supported with remote hosts.""",
    )
    aes_256: bool = Field(
        alias="aes-256",
        description="""Select whether the AES-256 encryption algorithm will be supported with remote hosts.""",
    )
    des: bool = Field(
        alias="des",
        description="""Select whether the DES encryption algorithm will be supported with remote hosts.""",
    )
    tdes: bool = Field(
        alias="tdes",
        description="""Select whether the Triple DES encryption algorithm will be supported with remote hosts.""",
    )
