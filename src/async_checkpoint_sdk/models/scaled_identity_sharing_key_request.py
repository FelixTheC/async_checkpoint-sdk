from pydantic import BaseModel, Field


class ScaledIdentitySharingKeyRequest(BaseModel):
    pdp_uid: str = Field(
        alias="pdp-uid", description="""Policy Definition Point object unique identifier."""
    )
    pep_uid: str = Field(
        alias="pep-uid", description="""Policy Enforcement Point object unique identifier."""
    )
