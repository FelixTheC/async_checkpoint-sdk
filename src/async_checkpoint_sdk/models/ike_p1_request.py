from .pydantic import BaseModel, Field


class IkeP1Request(BaseModel):
    encryption_algorithm: str = Field(
        alias="encryption-algorithm",
        description="""The encryption algorithm to be used.""",
    )
    data_integrity: str = Field(
        alias="data-integrity", description="""The hash algorithm to be used."""
    )
    diffie_hellman_group: str = Field(
        alias="diffie-hellman-group",
        description="""The Diffie-Hellman group to be used.""",
    )
    use_standard_proposal: bool = Field(
        alias="use-standard-proposal",
        description="""Indicates whether to use a proposal with a single Diffie-Hellman group.""",
    )
    use_multiple_key_exchanges: bool = Field(
        alias="use-multiple-key-exchanges",
        description="""Indicates whether to use a proposal with Multiple Key Exchanges.""",
    )
    multiple_key_exchanges: str = Field(
        alias="multiple-key-exchanges",
        description="""Name of the Multiple Key Exchanges proposal object.""",
    )
    ike_p1_rekey_time: int = Field(
        alias="ike-p1-rekey-time",
        description="""Indicates the time interval for IKE phase 1 renegotiation.""",
    )
    ike_p1_rekey_time_unit: str = Field(
        alias="ike-p1-rekey-time-unit",
        description="""Indicates the time unit for [ike-p1-rekey-time-unit] parameter, rounded up to minutes scale.""",
    )
