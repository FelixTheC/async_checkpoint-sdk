from .pydantic import BaseModel, Field


class AggressiveAgingReply(BaseModel):
    default_timeout: int = Field(
        alias="default-timeout",
        description="""Default aggressive aging timeout in seconds.""",
    )
    enable: bool = Field(alias="enable", description="""N/A""")
    timeout: int = Field(alias="timeout", description="""Aggressive aging timeout in seconds.""")
    use_default_timeout: bool = Field(alias="use-default-timeout", description="""N/A""")
