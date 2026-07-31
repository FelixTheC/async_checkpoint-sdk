from .pydantic import BaseModel, Field


class SecurIdSettingsRequest(BaseModel):
    token_card_type: str = Field(
        alias="token-card-type",
        description="""Token card type for SecurID authentication.""",
    )
