from pydantic import BaseModel, Field


class AdvancedPropertiesRequest(BaseModel):
    support_ip_compression: bool = Field(
        alias="support-ip-compression",
        description="""Indicates whether to support IP compression.""",
    )
    use_aggressive_mode: bool = Field(
        alias="use-aggressive-mode",
        description="""Indicates whether to use aggressive mode.""",
    )
