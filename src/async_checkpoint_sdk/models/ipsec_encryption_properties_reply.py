from .ipsec_support_data_integrity_reply import IpsecSupportDataIntegrityReply
from .ipsec_support_encryption_algs_reply import IpsecSupportEncryptionAlgsReply
from .pydantic import BaseModel, Field


class IpsecEncryptionPropertiesReply(BaseModel):
    support_encryption_algorithms: IpsecSupportEncryptionAlgsReply = Field(
        alias="support-encryption-algorithms",
        description="""Select the encryption algorithms that will be supported with remote hosts.""",
    )
    use_encryption_algorithm: str = Field(
        alias="use-encryption-algorithm",
        description="""Choose the encryption algorithm that will have the highest priority of the selected algorithms. If given a choice of more that one encryption algorithm to use, the algorithm selected in this field will be used.""",
    )
    support_data_integrity: IpsecSupportDataIntegrityReply = Field(
        alias="support-data-integrity",
        description="""Select the hash algorithms that will be supported with remote hosts to ensure data integrity.""",
    )
    use_data_integrity: str = Field(
        alias="use-data-integrity",
        description="""The hash algorithm chosen here will be given the highest priority if more than one choice is offered.""",
    )
    enforce_encryption_alg_and_data_integrity_on_all_users: bool = Field(
        alias="enforce-encryption-alg-and-data-integrity-on-all-users",
        description="""Enforce Encryption Algorithm and Data Integrity on all users.""",
    )
