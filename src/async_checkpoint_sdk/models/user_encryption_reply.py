from pydantic import BaseModel, Field


class UserEncryptionReply(BaseModel):
    ike: bool = Field(alias="ike", description="""IKE users encryption enabled.""")
    public_key: bool = Field(alias="public-key", description="""IKE public key enabled.""")
    shared_secret: bool = Field(alias="shared-secret", description="""IKE shared secret enabled.""")
