from pydantic import BaseModel, Field


class UserTemplateEncryptionRequest(BaseModel):
    enable_ike: bool = Field(alias="enable-ike", description="""Enable IKE encryption for users.""")
    enable_public_key: bool = Field(
        alias="enable-public-key", description="""Enable IKE public key."""
    )
    enable_shared_secret: bool = Field(
        alias="enable-shared-secret", description="""Enable IKE shared secret."""
    )
