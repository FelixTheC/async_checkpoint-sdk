from .certs_and_pki_global_properties_request import CertsAndPkiGlobalPropertiesRequest
from .pydantic import BaseModel, Field


class GlobalPropertiesAdvancedConfRequest(BaseModel):
    certs_and_pki: CertsAndPkiGlobalPropertiesRequest = Field(
        alias="certs-and-pki",
        description="""Configure Certificates and PKI properties.""",
    )
    keep_ike_sas: bool = Field(
        alias="keep-ike-sas",
        description="""Enabled: Keep ALL IKEv1 phase 1 Security Associations (SA) upon policy installation.<br>Disabled: Delete ALL IKEv1 phase 1 Security Associations (SA) upon policy installation.""",
    )
