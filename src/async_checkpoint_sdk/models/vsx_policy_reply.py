from .date import Date
from .pydantic import BaseModel, Field


class VsxPolicyReply(BaseModel):
    policy_installation_date: Date = Field(
        alias="policy-installation-date", description="""Policy installation date."""
    )
    policy_installation_status: str = Field(
        alias="policy-installation-status",
        description="""Policy installation status.""",
    )
    policy_name: str = Field(alias="policy-name", description="""Policy name.""")
