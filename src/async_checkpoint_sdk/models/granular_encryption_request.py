from ike_p1_request_new import IkeP1RequestNew
from ike_p2_request_new import IkeP2RequestNew
from pydantic import BaseModel, Field


class GranularEncryptionRequest(BaseModel):
    internal_gateway: str = Field(
        alias="internal-gateway",
        description="""Internally managed Check Point gateway identified by name or UID, or 'Any' for all internal-gateways participants in this community.""",
    )
    external_gateway: str = Field(
        alias="external-gateway",
        description="""Externally managed or 3rd party gateway identified by name or UID.""",
    )
    encryption_method: str = Field(
        alias="encryption-method", description="""The encryption method to be used."""
    )
    encryption_suite: str = Field(
        alias="encryption-suite", description="""The encryption suite to be used."""
    )
    ike_phase_1: IkeP1RequestNew = Field(
        alias="ike-phase-1",
        description="""Ike Phase 1 settings. Only applicable when the encryption-suite is set to [custom].""",
    )
    ike_phase_2: IkeP2RequestNew = Field(
        alias="ike-phase-2",
        description="""Ike Phase 2 settings. Only applicable when the encryption-suite is set to [custom].""",
    )
