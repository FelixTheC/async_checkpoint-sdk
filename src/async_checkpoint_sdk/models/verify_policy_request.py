from pydantic import BaseModel, Field


class VerifyPolicyRequest(BaseModel):
    policy_package: str = Field(
        alias="policy-package", description="""Policy package identified by the name or UID."""
    )
