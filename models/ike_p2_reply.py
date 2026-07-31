from multiple_key_exchanges_reply import MultipleKeyExchangesReply
from pydantic import BaseModel, Field


class IkeP2Reply(BaseModel):
    encryption_algorithm: str = Field(
        alias="encryption-algorithm",
        description="""The encryption algorithm to be used.""",
    )
    data_integrity: str = Field(
        alias="data-integrity", description="""The hash algorithm to be used."""
    )
    ike_p2_use_pfs: bool = Field(
        alias="ike-p2-use-pfs",
        description="""Indicates whether Perfect Forward Secrecy (PFS) is being used for IKE phase 2.""",
    )
    ike_p2_pfs_dh_grp: str = Field(
        alias="ike-p2-pfs-dh-grp",
        description="""The Diffie-Hellman group to be used.""",
    )
    use_standard_proposal: bool = Field(
        alias="use-standard-proposal",
        description="""Indicates whether to use a proposal with a single Diffie-Hellman group when PFS is enabled.""",
    )
    use_multiple_key_exchanges: bool = Field(
        alias="use-multiple-key-exchanges",
        description="""Indicates whether to use a proposal with Multiple Key Exchanges when PFS is enabled.""",
    )
    multiple_key_exchanges: MultipleKeyExchangesReply = Field(
        alias="multiple-key-exchanges",
        description="""Multiple Key Exchanges proposal object to use when PFS is enabled and multiple key exchanges are configured.""",
    )
    ike_p2_rekey_time: int = Field(
        alias="ike-p2-rekey-time",
        description="""Indicates the time interval for IKE phase 2 renegotiation.""",
    )
