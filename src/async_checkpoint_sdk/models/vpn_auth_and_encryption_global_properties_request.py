from .encryption_algorithms_global_properties_request import (
    EncryptionAlgorithmsGlobalPropertiesRequest,
)
from .pydantic import BaseModel, Field


class VpnAuthAndEncryptionGlobalPropertiesRequest(BaseModel):
    encryption_algorithms: EncryptionAlgorithmsGlobalPropertiesRequest = Field(
        alias="encryption-algorithms",
        description="""Select the methods negotiated in IKE phase 2 and used in IPSec connections.""",
    )
    encryption_method: str = Field(
        alias="encryption-method", description="""Select the encryption method."""
    )
    pre_shared_secret: bool = Field(
        alias="pre-shared-secret",
        description="""the user password is specified in the Authentication tab in the user's IKE properties (in the user properties window: Encryption tab > Edit).""",
    )
    support_legacy_auth_for_sc_l2tp_nokia_clients: bool = Field(
        alias="support-legacy-auth-for-sc-l2tp-nokia-clients",
        description="""Support Legacy Authentication for SC (hybrid mode), L2TP (PAP) and Nokia clients (CRACK).""",
    )
    support_legacy_eap: bool = Field(
        alias="support-legacy-eap",
        description="""Support Legacy EAP (Extensible Authentication Protocol).""",
    )
    support_l2tp_with_pre_shared_key: bool = Field(
        alias="support-l2tp-with-pre-shared-key",
        description="""Use a centrally managed pre-shared key for IKE.""",
    )
    l2tp_pre_shared_key: str = Field(
        alias="l2tp-pre-shared-key",
        description="""Type in the pre-shared key.<br>Available only if support-l2tp-with-pre-shared-key is set to true.""",
    )
