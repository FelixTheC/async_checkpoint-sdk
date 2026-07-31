from .ike_support_data_integrity_request import IkeSupportDataIntegrityRequest
from .ike_support_encryption_algs_request import IkeSupportEncryptionAlgsRequest
from .pydantic import BaseModel, Field
from .support_d_h_groups_request import SupportDHGroupsRequest


class IkeEncryptionPropertiesRequest(BaseModel):
    support_encryption_algorithms: IkeSupportEncryptionAlgsRequest = Field(
        alias="support-encryption-algorithms",
        description="""Select the encryption algorithms that will be supported with remote hosts.""",
    )
    use_encryption_algorithm: str = Field(
        alias="use-encryption-algorithm",
        description="""Choose the encryption algorithm that will have the highest priority of the selected algorithms. If given a choice of more that one encryption algorithm to use, the algorithm selected in this field will be used.""",
    )
    support_data_integrity: IkeSupportDataIntegrityRequest = Field(
        alias="support-data-integrity",
        description="""Select the hash algorithms that will be supported with remote hosts to ensure data integrity.""",
    )
    use_data_integrity: str = Field(
        alias="use-data-integrity",
        description="""The hash algorithm chosen here will be given the highest priority if more than one choice is offered.""",
    )
    support_diffie_hellman_groups: SupportDHGroupsRequest = Field(
        alias="support-diffie-hellman-groups",
        description="""Select the Diffie-Hellman groups that will be supported with remote hosts.""",
    )
    use_diffie_hellman_group: str = Field(
        alias="use-diffie-hellman-group",
        description="""SecureClient users utilize the Diffie-Hellman group selected in this field.""",
    )
