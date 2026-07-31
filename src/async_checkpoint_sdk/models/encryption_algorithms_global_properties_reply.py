from ike_encryption_properties_reply import IkeEncryptionPropertiesReply
from ipsec_encryption_properties_reply import IpsecEncryptionPropertiesReply
from pydantic import BaseModel, Field


class EncryptionAlgorithmsGlobalPropertiesReply(BaseModel):
    ike: IkeEncryptionPropertiesReply = Field(
        alias="ike", description="""Configure the IKE Phase 1 settings."""
    )
    ipsec: IpsecEncryptionPropertiesReply = Field(
        alias="ipsec", description="""Configure the IPSEC Phase 2 settings."""
    )
