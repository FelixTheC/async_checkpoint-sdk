from pydantic import BaseModel, Field


class VerifyLicReply(BaseModel):
    actual_gateways: int = Field(
        alias="actual-gateways", description="""Overall number of gateways in domain."""
    )
    license_status: str = Field(
        alias="license-status", description="""Management license status."""
    )
    licensed_gateways: str = Field(
        alias="licensed-gateways", description="""Number of gateways covered by domain license."""
    )
