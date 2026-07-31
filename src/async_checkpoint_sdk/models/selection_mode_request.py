from .pydantic import BaseModel, Field


class SelectionModeRequest(BaseModel):
    enable: bool = Field(alias="enable", description="""""")
    mode: int = Field(
        alias="mode",
        description="""The mode as integer. [0 - Verified, 1 - MS - Not verified, 2 - Network - Not verified].""",
    )
