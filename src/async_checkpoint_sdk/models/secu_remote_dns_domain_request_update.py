from .pydantic import BaseModel, Field


class SecuRemoteDnsDomainRequestUpdate(BaseModel):
    maximum_prefix_label_count: int = Field(
        alias="maximum-prefix-label-count",
        description="""Maximum number of matching labels preceding the suffix.""",
    )
    new_domain_suffix: str = Field(
        alias="new-domain-suffix", description="""New DNS Domain suffix."""
    )
