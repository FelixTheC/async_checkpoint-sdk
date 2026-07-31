from .pydantic import BaseModel, Field


class SecurIdSettingsRequestNew(BaseModel):
    token_card_type: str = Field(
        alias="token-card-type",
        description="""Token card type: any, key-fob, pinpad, software, token.""",
    )
