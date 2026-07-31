from pydantic import BaseModel, Field


class SecurIdSettingsRequest(BaseModel):
    server: str = Field(
        alias="server", description="""SecurID server object identified by name or UID."""
    )
    token_card_type: str = Field(
        alias="token-card-type", description="""Token card type for SecurID authentication."""
    )
