from ike_encryption_properties_request import IkeEncryptionPropertiesRequest
from ipsec_encryption_properties_request import IpsecEncryptionPropertiesRequest
from pydantic import BaseModel, Field


class EncryptionAlgorithmsGlobalPropertiesRequest(BaseModel):
    ike: IkeEncryptionPropertiesRequest = Field(
        alias="ike", description="""Configure the IKE Phase 1 settings."""
    )
    ipsec: IpsecEncryptionPropertiesRequest = Field(
        alias="ipsec", description="""Configure the IPSEC Phase 2 settings."""
    )
