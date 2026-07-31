from pydantic import BaseModel, Field


class SecuRemoteDnsDomainReply(BaseModel):
    domain_suffix: str = Field(
        alias="domain-suffix", description="""DNS Domain suffix."""
    )
    maximum_prefix_label_count: int = Field(
        alias="maximum-prefix-label-count",
        description="""Maximum number of matching labels preceding the suffix.""",
    )
