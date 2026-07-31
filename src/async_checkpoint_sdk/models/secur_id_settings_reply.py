from api_object_standard_identifier import ApiObjectStandardIdentifier
from pydantic import BaseModel, Field


class SecurIdSettingsReply(BaseModel):
    server: ApiObjectStandardIdentifier = Field(
        alias="server", description="""SecurID server object with name and UID."""
    )
    token_card_type: str = Field(
        alias="token-card-type",
        description="""Token card type: any, key-fob, pinpad, software, token.""",
    )
