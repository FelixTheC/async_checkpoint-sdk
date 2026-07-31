from .pydantic import BaseModel, Field


class SecuRemoteDnsDomainRequestNew(BaseModel):
    maximum_prefix_label_count: int = Field(
        alias="maximum-prefix-label-count",
        description="""Maximum number of matching labels preceding the suffix.""",
    )
