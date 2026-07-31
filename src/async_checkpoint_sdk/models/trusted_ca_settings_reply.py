from .pydantic import BaseModel, Field


class TrustedCaSettingsReply(BaseModel):
    automatic_update: bool = Field(
        alias="automatic-update",
        description="""Whether the trusted CAs package should be updated automatically.""",
    )
