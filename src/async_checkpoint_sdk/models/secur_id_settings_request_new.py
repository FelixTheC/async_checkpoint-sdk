from pydantic import BaseModel, Field


class SecurIdSettingsRequestNew(BaseModel):
    server: str = Field(
        alias="server", description="""SecurID server object identified by name or UID."""
    )
    token_card_type: str = Field(
        alias="token-card-type",
        description="""Token card type: any, key-fob, pinpad, software, token.""",
    )
